import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2, "Пароли не должны совпадать"