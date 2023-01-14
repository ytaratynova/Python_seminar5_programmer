# Создайте программу для игры в ""Крестики-нолики"".

from random import randint 

def PrintTable(ttt_list):
    print('\n-----------------')
    for i in range(0, 3):
        print(f'| {ttt_list[i]} |', end = ' ')
    print('\n-----------------')
    for i in range(3, 6):
        print(f'| {ttt_list[i]} |', end = ' ')
    print('\n-----------------')
    for i in range(6, 9):
        print(f'| {ttt_list[i]} |', end = ' ')
    print('\n-----------------')


def OneStep(ttt_list, player, count):
    step = 0
    if count % 2 != 0:
       put = 'X'
    else:
       put = '0'
    while step == 0:
        step = int(input(f'{player}, на какую позицию ставим {put}? '))
        while step > 9 or step < 1:
            step = int(input(f'Некорректный ввод! {player}, на какую позицию ставим {put}? '))

        if ttt_list[step-1] == step:
           ttt_list[step-1] = put
        else:
            step = 0
            print('Данная позиция занята!')
    return(ttt_list)


def IfWin(ttt_list):
    win = 0
    win_list = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_list:
        if ttt_list[each[0]] == ttt_list[each[1]] == ttt_list[each[2]] == 'X' or ttt_list[each[0]] == ttt_list[each[1]] == ttt_list[each[2]] == '0':
            win = 1
    return win


tic_tac_toe = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player01 = input('Введите имя первого игрока: ')
player02 = input('Введите имя второго игрока: ')
print()

turn = randint(1, 2)
if turn == 1:
    print(f"Первый ход определен жеребьевкой: ходит {player01}!")
else:
    print(f"Первый ход определен жеребьевкой: ходит {player02}!")

win = 0
step_count = 1
PrintTable(tic_tac_toe)

while win == 0 and step_count < 10:
    if turn == 1:
       tic_tac_toe = OneStep(tic_tac_toe, player01, step_count)
       turn = 2
    else:  
       tic_tac_toe = OneStep(tic_tac_toe, player02, step_count)
       turn = 1
    PrintTable(tic_tac_toe)
    win = IfWin(tic_tac_toe)
    step_count += 1

if turn == 1 and win == 1:
    print(f'{player02}, ура! Вы выиграли!')
elif turn == 2 and win == 1:
    print(f'{player01}, ура! Вы выиграли!')
else:
    print('Игра закончилась ничьей!')



