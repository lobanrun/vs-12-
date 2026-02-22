import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_passwords12_bySanya():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2 

def testpasswordlenght_sanya():
    expected_lenght = 12
    password = generate_password(expected_lenght)
    assert len(password) == expected_lenght

def testspecialsymbol():
    special = string.punctuation
    password = generate_password(10)
    assert any(c in special for c in password)


"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""