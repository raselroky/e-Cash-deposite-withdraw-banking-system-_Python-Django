from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from . models import Register
from transaction.models import E_cash

@api_view(['GET','POST'])
def RegisterApi(request):
    if request.method=='POST':
        name=request.data['name']
        username=request.data['username']
        email=request.data['email']
        mobile=request.data['mobile']
        password=request.data['password']
        retype_password=request.data['retype_password']

    s=str(password)
    if (Register.objects.filter(username=username).exists()):
        return Response({"Message":"This username is already taken,try Another!"})

    if(len(str(password))<6 and len(str(retype_password))<6):
        return Response({"Message":"Password Too short! try Again."})

    if(password!=retype_password):
        return Response({"Message":"Two password didn't matched ,try agian!"})
    
    if(any(map(str.isdigit, s))==False or any(map(str.isalpha, s))==False):
        return Response({"Message":"Character or Number missing ,try again!"})  

    user=Register(name=name,username=username,email=email,mobile=mobile,password=password,retype_password=retype_password)
    user.save()
    trans=E_cash(name=name,username=username,deposite_withdraw='',amount='0',total_amount='0')
    trans.save()
    return Response({"Message":"Registration Successfully Done."})

@api_view(['GET','POST']) 
def LoginApi(request):
    if request.method=='POST':
        username=request.data['username']
        password=request.data['password']

    username1=Register.objects.filter(username=username,password=password).exists()
    password1=Register.objects.filter(password=password,username=username).exists()

    if(username1 and password1):
        return Response({"Message":"Successfully Login!"})
    else:
        return Response({"Message":"Error, complete your registration then try login."})
    
    
    
