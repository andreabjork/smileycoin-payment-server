from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class PaymentRequest(models.Model):
    address = models.CharField(max_length=60)
    amount = models.DecimalField()
    confirmation = models.BooleanField()
