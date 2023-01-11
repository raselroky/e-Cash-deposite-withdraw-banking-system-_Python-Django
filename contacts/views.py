from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework import generics,mixins


class ConactUs(APIView):

    def post(self,request):
        serializer=ContactSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"Successfully Sended Contact information !"})
        return Response({"Message":"Error"})
    

    

