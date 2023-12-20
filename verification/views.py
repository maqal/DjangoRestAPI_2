from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import *
from .serializer import *

# Create your views here.
class VerificationList(generics.ListCreateAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerialier
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class VerificationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerialier
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]