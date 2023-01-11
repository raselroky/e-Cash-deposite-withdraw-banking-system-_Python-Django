from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .models import Register
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import generics,mixins
from transaction.models import E_cash


class RegisterAPI(APIView):
    def post(self,request):
        serializer= RegisterSerializer(data=request.data)
        if serializer.is_valid():
            password=request.data['password']
            if(password!=request.data['retype_password']):
                return Response({"Message":"Password did not matched!"})
            if(len(str(password))<6 and len(str(request.data['retype_password']))<6):
                return Response({"Message":"Password Too short! try Again."})
            if(any(map(str.isdigit, password))==False or any(map(str.isalpha, password))==False):
                return Response({"Message":"Character or Number missing ,try again!"})

            serializer.save()
            trans=E_cash(name=request.data['name'],username=request.data['username'],deposite_withdraw='',amount='0',total_amount='0')
            trans.save()
            return Response({"Message":"Successfully Registration complete!"})
        
        return Response({"error":"Not valid!"})
                 



class LoginAPI(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']

        username1=Register.objects.filter(username=username,password=password).exists()
        password1=Register.objects.filter(password=password,username=username).exists()

        if(username1 and password1):
            return Response({"Message":"Successfully Login!"})
        else:
            return Response({"Message":"Error, complete your registration then try login."})
    
    
    
