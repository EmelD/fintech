import uuid
from django.db import models


class Transaction(models.Model):
    wallet_id = models.ForeignKey(
        "wallet.Wallet",
        on_delete=models.PROTECT,
    )
    txid = models.UUIDField(default=uuid.uuid4, unique=True)
    amount = models.DecimalField(max_digits=50, decimal_places=18)
