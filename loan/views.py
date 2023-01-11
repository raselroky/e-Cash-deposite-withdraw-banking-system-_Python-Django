from django.shortcuts import render
from .models import Loan
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework import generics,mixins
from .serializers import LoanSerializer

class LoanPossible(APIView):
    
    def post(self,request):
        serializer=LoanSerializer(data=request.data)
        if(serializer.is_valid()):
            s=int(request.data['salary'])
            l=int(request.data['loan'])
        
            if(26000<=s and s<=40000):
                if(l<=300000):
                    return Response({"Message":"Yes,Your loan is possible,Contact Bank Manager"})
                else:
                    return Response({"Message":"Not possible"})
            elif(40000<s and s<=60000):
                if(l<=500000):
                    return Response({"Message":"Yes,Your loan is possible,Contact Bank Manager"})
                else:
                    return Response({"Message":"Not possible"})
            elif(60000<s and s<=80000):
                if(l<=600000):
                    return Response({"Message":"Yes,Your loan is possible,Contact Bank Manager"})
                else:
                    return Response({"Message":"Not possible"})
            elif(80000<s and s<=100000):
                if(l<=700000):
                    return Response({"Message":"Yes,Your loan is possible,Contact Bank Manager"})
                else:
                    return Response({"Message":"Not possible"})
