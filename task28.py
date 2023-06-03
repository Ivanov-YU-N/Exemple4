#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. #Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)
number_one = int(input("Введите число = "))
number_two = int(input("Введите число = "))
print(summa(number_one, number_two))