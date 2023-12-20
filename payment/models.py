from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
DURATION_CHOICES = (
    ("MONTHLY", "Monthly"),
    ("ANNUAL", "Annual"),
)

# generate token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)
    

class Payment(models.Model):
    duration = models.CharField(max_length=50, choices = DURATION_CHOICES, default = 'Monthly')
    amount = models.IntegerField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    initial_payment = models.TimeField(auto_now_add=True)
    updated_payment = models.TimeField(auto_now=True)
    