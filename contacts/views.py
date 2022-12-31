from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from contacts.models import Contact

@api_view(['GET','POST'])
def Contact_Us(request):
    if(request.method=='POST'):
        First_Name=request.data['First_Name']
        Last_Name=request.data['Last_Name']
        Mobile=request.data['Mobile']
        Email=request.data['Email']
        Purpose=request.data['Purpose']
        Message=request.data['Message']
    
    con=Contact(First_Name=First_Name,Last_Name=Last_Name,Mobile=Mobile,Email=Email,Purpose=Purpose,Message=Message)
    con.save()
    return Response({"Message":"Successfully Sended Contact information !"})
    

    

