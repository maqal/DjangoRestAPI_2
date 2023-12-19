from django.urls import path
from .views import *

urlpatterns = [
    path('', VerificationList.as_view()),
    path('<int:pk>', VerificationDetails.as_view()),
]