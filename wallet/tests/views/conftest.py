from typing import Any
from typing import Callable
from typing import Dict

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def get_wallets(
    client: APIClient,
) -> Callable[..., Dict[Any, Any]]:
    def _() -> Dict[Any, Any]:
        return client.get('/v1/wallets/')

    return _
