# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    count_1 = False
    count_2 = False
    count_3 = False
    for i in password:
        if i.islower():
            count_1 = True
        elif i.isupper():
            count_2 = True
        elif i.isdigit():
            count_3 = True
    return count_1 and count_2 and count_3
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))