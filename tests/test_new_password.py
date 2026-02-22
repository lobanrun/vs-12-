import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100) 
    for char in password:
        assert char in valid_characters

def test_default(): 
    """ Тест проверяет значение по умолчанию """
    assert len(generate_password()) == 12

def test_hristofor():
    pass 
