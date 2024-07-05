from django.core.management import call_command

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings

    settings.DATABASES['default']['NAME'] = 'fintech_test'
    settings.DATABASES['default']['PORT'] = '3307'

    call_command('migrate')

    yield

