from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    district = models.CharField(max_length=50)
    loan_amount = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
class CallbackRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    preferred_time = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    