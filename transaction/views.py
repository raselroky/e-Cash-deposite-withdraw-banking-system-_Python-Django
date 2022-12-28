from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from transaction.models import E_cash
from register.models import Register


@api_view(['GET','POST'])
def Transaction(request):
    if(request.method=='POST'):
        username=request.data['username']
        deposite_withdraw=request.data['deposite_withdraw']
        amount=request.data['amount']
    
    cnt=E_cash.objects.filter(username=username).count()
    s=E_cash.objects.filter(username=username).values().last()
    
    name=s['name']
    if(deposite_withdraw=='withdraw' and s['total_amount']=='0'):
        return Response({"Message":"Insufficient Balance !"})
    elif(deposite_withdraw=='deposite'):
        s['deposite_withdraw']=deposite_withdraw
        am=int(amount)
        t_am=int(s['total_amount'])
        d=str(am+t_am)
        s['total_amount']=str(d)
    elif(deposite_withdraw=='withdraw'):
        s['deposite_withdraw']=deposite_withdraw
        am=int(amount)
        t_am=int(s['total_amount'])
        if(t_am<am):
            return Response({"Message":"Insufficient Balance !"})
        else:
            d=str(t_am-am)
            s['total_amount']=str(d)
    trans=E_cash(name=name,username=username,deposite_withdraw=s['deposite_withdraw'],amount=amount,total_amount=s['total_amount'])
    trans.save()
    return Response({"Message":"ALL ok!"})        

    

