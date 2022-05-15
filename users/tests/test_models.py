import pytest

from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username="usuario_teste",
        email="usuario_teste@email.com",
        password="passw0rd",
        cidade="cidade_teste",
        estado="estado_teste",
        telefone="(011)2222-9090",
    )

    assert user.username == "usuario_teste"
    assert user.email == "usuario_teste@email.com"
    assert user.cidade == "cidade_teste"
    assert user.estado == "estado_teste"
    assert user.telefone == "(011)2222-9090"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
        username="admin_teste",
        email="admin_teste@email.com",
        password="passw0rd"
    )

    assert user.username == "admin_teste"
    assert user.email == "admin_teste@email.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser
