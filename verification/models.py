from django.db import models

# Create your models here.
class Verification(models.Model):
    business_name = models.CharField(max_length=150)
    fullname = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    attachment = models.FileField(upload_to='img', max_length=500)
    link_1 = models.CharField(max_length=50)
    link_2 = models.CharField(max_length=50)
    link_3 = models.CharField(max_length=50)
    selfie = models.FileField(upload_to='img', max_length=500)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
