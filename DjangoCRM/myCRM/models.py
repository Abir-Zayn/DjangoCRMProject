from django.db import models
# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    usermail = models.EmailField(max_length=30)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    
    