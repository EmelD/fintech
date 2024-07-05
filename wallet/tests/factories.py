import factory

from wallet.models import Wallet


class CustomerFactory(factory.DjangoModelFactory):

    class Meta:
        model = Wallet
