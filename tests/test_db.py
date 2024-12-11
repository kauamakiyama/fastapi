from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_create_user(session):
    user = User(
        username="kaua",
        email="kaua@bernardo.com",
        password="123"
        )
    session.add(user)
    session.commit()

        # Buscando o usuário pelo username correto
    result = session.scalar(select(User).where(User.username == "kaua"))

    # Validando se o nome do usuário está correto
    assert result is not None  # Certifica-se de que o resultado não é None
    assert result.username == "kaua"
