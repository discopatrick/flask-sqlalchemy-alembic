from backend.models import User

def test_user_model_repr():
    user = User(name='patrick', fullname='Disco Patrick', password='disco123!')

    assert repr(user) == ("<User(name='patrick', fullname='Disco Patrick', "
        "password='disco123!')>")
