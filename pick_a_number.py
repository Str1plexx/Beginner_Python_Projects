from random import *
num = randint(1, 100)
choise = 0
print('Добро пожаловать в числовую угодайку!')
print('Для завершения игры введите "-1"')
while num != choise:
    choise = int(input('Введите число в диапозоне от 1 до 100: '))
    if not 1 <= choise <= 100:
        print('Может ты выберешь число в этом диапазоне(1, 100)')
        continue
    if choise == -1:
        break
print('Спасибо за игру!')

