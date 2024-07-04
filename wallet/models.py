from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=200)
    balance = models.DateTimeField("date published")
