from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PaymentSerialier(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'