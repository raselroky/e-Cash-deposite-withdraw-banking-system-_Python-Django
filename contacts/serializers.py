from rest_framework import serializers
from django.forms import fields
from . models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('__all__')