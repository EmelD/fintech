import pytest
from django.core.management import call_command


@pytest.mark.django_db
@pytest.fixture(scope='session')
def db_setup() -> None:
    call_command('migrate')
