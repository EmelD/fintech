from typing import Any
from typing import Callable
from typing import Dict

import pytest

pytestmark = pytest.mark.django_db


def test_transaction_ok(
    get_transactions: Callable[..., Dict[Any, Any]],
):
    response = get_transactions()


def test_transaction_pagination(
    get_transactions: Callable[..., Dict[Any, Any]],
):
    response = get_transactions()


def test_transaction_empty(
    get_transactions: Callable[..., Dict[Any, Any]],
):
    response = get_transactions()


def test_transaction_search(
    get_transactions: Callable[..., Dict[Any, Any]],
):
    response = get_transactions()


def test_transaction_ordering(
    get_transactions: Callable[..., Dict[Any, Any]],
):
    response = get_transactions()
