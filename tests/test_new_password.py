import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
def test_default(): #Ilja Prusakovs
    """ Тест проверяет значение по умолчанию """
    assert len(generate_password()) == 12
    
def test_length_roma():
    password = generate_password(100)
    assert len(password) == 100
def test_razlychye_roma():
    passwordone = generate_password(50)
    passwordtwo = generate_password(50)
    assert passwordone != passwordtwo

def test_password_length_of_characters_by_ivan():
    """Тест, что при генерации пароля пароль генерируется нужной длинны"""
    password = generate_password(80)
    assert len(password) == 80

    
def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2, "Пароли не должны совпадать"

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

   
def test_password_not_s():
    """Тест на совпадение генерации by s1koi"""
    password1 = generate_password(10) 
    password2 = generate_password(10)
    assert password1 != password2
    
def test_password_len():
    """Тест на проверку длины by s1koi"""
    password1 = generate_password(10)  
    leng = len(password1)
    assert leng == 10



def test_lenght_by_nikita_a():
    assert len(generate_password(10)) == 10
    
def test_passwords_are_different_by_nikita_a():
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2
    
def test_thanks_for_use_our_project_by_flizard25():
    print("Спасибо что воспользовались нашим проектом!")
