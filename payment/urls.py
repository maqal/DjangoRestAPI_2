from django.urls import path
from .views import *

urlpatterns = [
    path('', PaymentList.as_view()),
    path('<int:pk>', PaymentDetails.as_view()),
]