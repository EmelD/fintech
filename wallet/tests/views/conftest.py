from collections import namedtuple
from typing import Callable, Optional
from urllib.parse import urlencode, urlunparse

import pytest
from rest_framework.response import Response
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def get_wallets(
    client: APIClient,
) -> Callable[..., Response]:
    def _(
        page: Optional[str] = None,
        search: Optional[str] = None,
        ordering: Optional[str] = None,
    ) -> Response:
        Components = namedtuple(  # type: ignore[misc]
            typename='Components',
            field_names=['scheme', 'netloc', 'url', 'path', 'query', 'fragment'],
        )

        query_params = {}
        if page:
            query_params['page'] = page
        if search:
            query_params['search'] = search
        if ordering:
            query_params['ordering'] = ordering

        url = urlunparse(
            Components(  # type: ignore[call-arg]
                scheme='',
                netloc='',
                query=urlencode(query_params),
                path='',
                url='/v1/wallets/',
                fragment='',
            )
        )

        return client.get(url)

    return _
