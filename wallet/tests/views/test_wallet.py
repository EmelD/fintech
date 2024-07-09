from typing import Callable

import pytest
from pampy import match
from rest_framework import status
from rest_framework.response import Response

pytestmark = pytest.mark.django_db


def test_wallet_ok(
    wallet_test_label: None, get_wallets: Callable[..., Response]
) -> None:
    response = get_wallets()

    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert match(
        data,
        {
            'count': int,
            'next': None,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': str,
            'balance': str,
        },
        True,
    )


def test_wallet_pagination__first_page(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets()

    assert response.status_code == status.HTTP_200_OK
    assert match(
        response.json(),
        {
            'count': int,
            'next': 'http://testserver/v1/wallets/?page=2',
            'previous': None,
            'results': list,
        },
        True,
    )


def test_wallet_pagination__last_page(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(page=2)

    assert response.status_code == status.HTTP_200_OK
    assert match(
        response.json(),
        {
            'count': int,
            'next': None,
            'previous': 'http://testserver/v1/wallets/',
            'results': list,
        },
        True,
    )


def test_wallet_search__by_label(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(search='test')

    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert match(
        data,
        {
            'count': 5,
            'next': None,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': 'test',
            'balance': str,
        },
        True,
    )


def test_wallet_search__by_unknown_label(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(search='unknown')

    assert response.status_code == status.HTTP_200_OK
    assert match(
        response.json(),
        {
            'count': 0,
            'next': None,
            'previous': None,
            'results': list,
        },
        True,
    )


def test_wallet_asc_ordering_by_label(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(ordering='label')

    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert match(
        data,
        {
            'count': int,
            'next': str,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': 'income',
            'balance': str,
        },
        True,
    )


def test_wallet_desc_ordering_by_label(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(ordering='-label')

    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert match(
        data,
        {
            'count': int,
            'next': str,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': 'test',
            'balance': str,
        },
        True,
    )


def test_wallet_asc_ordering_by_balance(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(ordering='balance')

    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert match(
        data,
        {
            'count': int,
            'next': str,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': 'test',
            'balance': str,
        },
        True,
    )


def test_wallet_desc_ordering_by_balance(
    wallet_test_label: None,
    wallet_income_label: None,
    wallet_interest_label: None,
    get_wallets: Callable[..., Response],
) -> None:
    response = get_wallets(ordering='-balance')

    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert match(
        data,
        {
            'count': int,
            'next': str,
            'previous': None,
            'results': list,
        },
        True,
    )
    assert match(
        data['results'][0],
        {
            'label': 'interest',
            'balance': str,
        },
        True,
    )
