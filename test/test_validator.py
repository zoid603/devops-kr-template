from validator import validate_email, validate_phone, validate_snils

def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+7999123") == False

def test_validate_snils():
    assert validate_snils("11223344595") == True
    assert validate_snils("112-233-445 95") == True
    assert validate_snils("12345678901") == False