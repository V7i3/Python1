# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.


def Week(day):
    if day == 6 or day == 7:
        return 'Да'
    elif 1 <= day <= 5:
        return 'Нет'
    else:
        return 'Нет такого дня'
    
x = int(input('Введите день недели цифрой: '))
print(Week(x))