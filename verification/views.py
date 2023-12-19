from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class VerificationList(generics.ListCreateAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerialier
    
class VerificationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerialier