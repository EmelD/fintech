import uuid
from django.db import models


class Transaction(models.Model):
    wallet_id = models.ForeignKey(
        "wallet.Wallet",
        on_delete=models.PROTECT,
    )
    txid = models.UUIDField(default=uuid.uuid4, editable=False)
    amount = models.IntegerField()
