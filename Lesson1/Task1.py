# Найдите сумму цифр трехзначного числа.

number = int(input("Введите число: "))
count = number//100 + number//10%10 + number%10
print("Сумма цифр числа = ", count)