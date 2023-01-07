from django.shortcuts import render
from .models import Loan
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET','POST'])
def LoanPossible(request):
    if(request.method=='POST'):
        salary=request.data['salary']
        loan=request.data['loan']
    
    s=int(salary)
    l=int(loan)
    print(s,l)
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
