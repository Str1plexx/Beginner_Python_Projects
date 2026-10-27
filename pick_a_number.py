from random import randint

print('Добро пожаловать в числовую угадайку!')


def new_game(n):
    num = randint(1, n)
    attempt = 1

    print('Для завершения игры введите "-1"')

    while True:
        print(f'Попытка №{attempt}')
        choice = int(input(f'Введите число в диапазоне от 1 до {n}: '))

        if choice == -1:
            break
        if not 1 <= choice <= n:
            print(f'Может ты выберешь число в этом диапазоне (1, {n})')
            continue
        if num > choice:
            print('Выбранное число меньше загаданного')
        elif num == choice:
            print('Вы выиграли!')
            break
        else:
            print('Выбранное число больше загаданного')
        attempt += 1


while True:
    n = int(input('Введите верхнюю границу: '))
    new_game(n)
    ans = input('Начать новую игру? (Да/Нет): ')
    if ans.strip().lower() == 'да':
        continue
    elif ans.strip().lower() == 'нет':
        break
    else:
        print('Некорректный ввод')

print('Спасибо за игру!')
