from rest_framework import serializers
from django.forms import fields
from . models import E_cash

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=E_cash
        fields=('__all__')