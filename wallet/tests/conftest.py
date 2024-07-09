from decimal import Decimal
from typing import Callable

import pytest

from wallet.tests.factories import WalletFactory


@pytest.fixture
def generate_wallets() -> Callable[[str, Decimal], None]:
    def inner(label: str, balance: Decimal, *, size: int = 5) -> None:
        WalletFactory.create_batch(size=size, label=label, balance=balance)

    return inner


@pytest.fixture
def wallet_test_label(
    generate_wallets: Callable[[str, Decimal], None],
) -> None:
    generate_wallets(label='test', balance=Decimal('10.999999999999999999'))  # type: ignore[call-arg]


@pytest.fixture
def wallet_income_label(
    generate_wallets: Callable[[str, Decimal], None],
) -> None:
    generate_wallets(label='income', balance=Decimal('20.999999999999999999'))  # type: ignore[call-arg]


@pytest.fixture
def wallet_interest_label(
    generate_wallets: Callable[[str, Decimal], None],
) -> None:
    generate_wallets(label='interest', balance=Decimal('30.999999999999999999'))  # type: ignore[call-arg]
