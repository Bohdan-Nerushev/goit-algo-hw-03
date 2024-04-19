#   =======№1=======
from datetime import datetime

def get_days_from_today(date:str) -> int:
    try:
        return (datetime.strptime(date, "%Y-%m-%d").date() - datetime.now().date()).days
    except ValueError:
        return ('Некоректний формат вводу !!!')
a = input("Введіть дату: ")
print(get_days_from_today(a))



#   =======№2=======
from random import randint

def get_numbers_ticket(minim = 1, maximum = 1000, quantity = 1):
    zahlen_list = []
    if 1000> minim>=1 and 1000>= maximum >=1 and maximum >= quantity >= minim:
        for _ in range(quantity):
            zahlen_list.append(randint(minim, maximum))
        zahlen_list=list(set(zahlen_list))
        while True:
            if quantity == len(list(set(zahlen_list))):
                zahlen_list.sort()
                return  zahlen_list
                break
            else:
                zahlen_list.append(randint(minim, maximum))
                zahlen_list=list(set(zahlen_list))
    else:
        return zahlen_list

min_zahlen, max_zahlen, count_zahlen =  int(input('Введіть мінімальне число: ')), int(input('Введіть максимальне число: ')), int(input('Введіть кількість чисел у вибірці: '))
print("Ваші лотерейні числа:", get_numbers_ticket(min_zahlen, max_zahlen, count_zahlen))

#   =======№3=======
import re


def normalize_phone(phone_number):
    formatted_phone = []

    pattern = r"[;,\-:!\.()+\\t n]"
    replacement = r""
    formatted_phone.append('+' + '38' + re.sub(pattern, replacement, phone_number)[-10:])
    return formatted_phone


phone = input('Введіть номер для корекції: ')

print(normalize_phone(phone))

#phone = [
#    "067\\t123 4567",
#    "(095) 234-5678\\n",
#    "+380 44 123 4567",
#    "380501234567",
#    "    +38(050)123-32-34",
#    "     0503451234",
#    "(050)8889900",
#    "38050-111-22-22",
#    "38050 111 22 11   ",
#]