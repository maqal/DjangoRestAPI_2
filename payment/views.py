from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerialier
    
class PaymentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerialier
