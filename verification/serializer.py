from rest_framework import serializers
from .models import *

class VerificationSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Verification
        fields = '__all__'