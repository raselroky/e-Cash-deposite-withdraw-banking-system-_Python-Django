from rest_framework import serializers
from django.forms import fields
from . models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=('__all__')