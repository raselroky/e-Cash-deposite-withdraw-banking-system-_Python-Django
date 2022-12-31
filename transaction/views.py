from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from transaction.models import E_cash
from register.models import Register
from django.db.models import F


@api_view(['GET','POST'])
def Transaction(request):
    if(request.method=='POST'):
        username=request.data['username']
        deposite_withdraw=request.data['deposite_withdraw']
        amount=request.data['amount']

    if (E_cash.objects.filter(username=username).exists()):
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
            trans=E_cash(name=name,username=username,deposite_withdraw=s['deposite_withdraw'],amount=amount,total_amount=s['total_amount'])
            trans.save()
            return Response({"Message":"Successfully Deposite your "+str(am)+" tk."})
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
            return Response({"Message":"Successfully Withdraw your "+str(am)+" tk."})

    else:
        return Response({"Error":"Type Correct Username!"})

@api_view(['POST','GET'])
def MyPresentData(request):
    if(request.method=='POST'):
        username=request.data['username']
    
    s=E_cash.objects.filter(username=username).values().last()
    
    return Response({"Present-Data":s})


@api_view(['POST','GET'])
def Transfer(request):
    if(request.method=='POST'):
        my_username=request.data['my_username']
        trans_username=request.data['trans_username']
        amount=request.data['amount']
    u1=E_cash.objects.filter(username=my_username).values().last()
    u2=E_cash.objects.filter(username=trans_username).values().last()

    am=int(amount)


    t_am_u1=int(u1['total_amount'])
    t_am_u2=int(u2['total_amount'])
    
    if(t_am_u1<am):
        return Response({"Message":"Insufficients Balanced!"})
    else:
        name1=u1['name']
        u1['deposite_withdraw']=str(am)+'tk Transfer to '+trans_username
        d1=t_am_u1-am
        u1['total_amount']=str(d1)
        trans1=E_cash(name=name1,username=my_username,deposite_withdraw=u1['deposite_withdraw'],amount=amount,total_amount=u1['total_amount'])
        trans1.save()

        name2=u2['name']
        u2['deposite_withdraw']=str(am)+'tk Transfer from '+my_username
        d2=t_am_u2+am
        u2['total_amount']=str(d2)
        trans2=E_cash(name=name2,username=trans_username,deposite_withdraw=u2['deposite_withdraw'],amount=amount,total_amount=u2['total_amount'])
        trans2.save()
    return Response({"Message":"Transaction Succeesfully Transfered ."})
