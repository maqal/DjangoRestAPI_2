from rest_framework import serializers
from .models import *

class PaymentSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'