from typing import Any
from typing import Callable
from typing import Dict

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_wallet_ok(
    get_wallets: Callable[..., Dict[Any, Any]]
):
    response = get_wallets()
    asd = ''


def test_wallet_pagination(
    get_wallets: Callable[..., Dict[Any, Any]],
):
    response = get_wallets()


def test_wallet_empty(
    get_wallets: Callable[..., Dict[Any, Any]],
):
    response = get_wallets()


def test_wallet_search(
    get_wallets: Callable[..., Dict[Any, Any]],
):
    response = get_wallets()


def test_wallet_ordering(
    get_wallets: Callable[..., Dict[Any, Any]],
):
    response = get_wallets()
