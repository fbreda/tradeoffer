import pytest
from users.models import User

from ..models import Offer

pytestmark = pytest.mark.django_db


def test_create_offer():
    offer = Offer.objects.create(
        offer_title="Cerveja Brahma 400ml",
        offer_description="Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem ",  # noqa
        author=User.objects.create_user(
            username='user_test_offer',
            email='user_test_offer@email.com',
            password='passw0rd'
        ),
    )

    assert offer.offer_title == "Cerveja Brahma 400ml"
    assert offer.offer_description == "Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem "  # noqa
    assert offer.is_active
