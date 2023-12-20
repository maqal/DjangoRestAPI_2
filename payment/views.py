from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import *
from .serializer import *

# Create your views here.
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerialier
    
    # authentication and perission
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    
class PaymentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerialier
    
     # authentication and perission
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    