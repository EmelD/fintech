import factory

from wallet.models import Wallet


class WalletFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Wallet
