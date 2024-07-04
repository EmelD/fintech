from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=65, decimal_places=18)
