from rest_framework import serializers
from django.forms import fields
from . models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=('__all__')