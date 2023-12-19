from django.db import models

# Create your models here.
DURATION_CHOICES = (
    ("MONTHLY", "Monthly"),
    ("ANNUAL", "Annual"),
)

class Payment(models.Model):
    duration = models.CharField(max_length=50, choices = DURATION_CHOICES, default = 'Monthly')
    amount = models.IntegerField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    initial_payment = models.TimeField(auto_now_add=True)
    updated_payment = models.TimeField(auto_now=True)
    