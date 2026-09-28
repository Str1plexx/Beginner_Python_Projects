from random import *

print('Добро пожаловать в числовую угодайку!')
def new_game(n)
    num = randint(1, n)
    choise = 0
    tru = 1

    print('Для завершения игры введите "-1"')

    while True:
        print(f' Попытка №{tru}')
        choise = int(input('Введите число в диапозоне от 1 до 100: '))

        if choise == -1:
            break
        if not 1 <= choise <= 100:
            print('Может ты выберешь число в этом диапазоне(1, 100)')
            continue
        if num > choise:
            print('Выбранное число меньше загаданного')
        elif num == choise:
            print('Вы выиграли!')
            break
        else:
            print('Выбранное число больше загаданного')
        tru += 1

while True:
    n = int(input('Введите верхнюю границу: '))
    new_game(n)
    ans = input('Начать новую игру? (Да/Нет)')
    if ans == 'Да':
        continue
    elif ans == 'Нет':
        break
    else:
        print('Некорректный ввод')
        
print('Спасибо за игру!')
