import re

def email_formati(email):
    shartlar = [
        re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None,
        len(email) <= 254,
        email.count('@') == 1,
        email.count('.') >= 1,
        email[0] != '.' and email[-1] != '.'
    ]
    
    return all(shartlar)

# Test qilish
print(email_formati('test@example.com'))  # True
print(email_formati('test@example'))  # False
print(email_formati('test@example.com.'))  # False
print(email_formati('test@example.com..com'))  # False
print(email_formati('test@example.com@'))  # False
print(email_formati('test@example.com.' * 100))  # False
