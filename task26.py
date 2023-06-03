#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую #степень B с помощью рекурсии.

def degree(a,b):
    if b == 0:
        return a
    else:
        return a*degree(a,b-1)

number = int(input("Введите число = "))
degree_namber = int(input("Введите степень числа = "))-1
print(degree(number, degree_namber))