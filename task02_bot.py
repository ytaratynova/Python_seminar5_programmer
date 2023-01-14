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


def BotStep(ttt_list, count):
    step = 0

    if count % 2 != 0:
       put = 'X'
       competitor = '0'
    else:
       put = '0'
       competitor = 'X'

    win_list = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) 
    
    for each in win_list:
        if (ttt_list[each[0]], ttt_list[each[1]], ttt_list[each[2]]).count(competitor) == 2:
            if ttt_list[each[0]] != '0' and ttt_list[each[0]] != 'X':
                ttt_list[each[0]] = put
                step = 1
                break
            elif ttt_list[each[1]] != '0' and ttt_list[each[1]] != 'X':
                 ttt_list[each[1]] = put
                 step = 1
                 break
            elif ttt_list[each[2]] != '0' and ttt_list[each[2]] != 'X':
                 ttt_list[each[2]] = put
                 step = 1
                 break
        else:
            if (ttt_list[each[0]], ttt_list[each[1]], ttt_list[each[2]]).count(put) == 2:
                if ttt_list[each[0]] != '0' and ttt_list[each[0]] != 'X':
                    ttt_list[each[0]] = put
                    step = 1
                    break
                elif ttt_list[each[1]] != '0' and ttt_list[each[1]] != 'X':
                    ttt_list[each[1]] = put
                    step = 1
                    break
                elif ttt_list[each[2]] != '0' and ttt_list[each[2]] != 'X':
                    ttt_list[each[2]] = put
                    step = 1
                    break
    
    diagonal_list = (0, 2, 6, 8)
    if step == 0:
        if ttt_list[4] != 'X' and ttt_list[4] != '0':
            ttt_list[4] = put
            step = 1
        else:
            for i in range(len(diagonal_list)):
                if ttt_list[diagonal_list[i]] != '0' and ttt_list[diagonal_list[i]] != 'X':
                   ttt_list[diagonal_list[i]] = put
                   step = 1
                   break

    other_list = (1, 3, 5, 7)
    if step == 0:
        for i in range(len(other_list)):
            if ttt_list[other_list[i]] != '0' and ttt_list[other_list[i]] != 'X':
                ttt_list[other_list[i]] = put
                step = 1
                break
    
    return ttt_list
    
        
def IfWin(ttt_list):
    win = 0
    win_list = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_list:
        if ttt_list[each[0]] == ttt_list[each[1]] == ttt_list[each[2]] == 'X' or ttt_list[each[0]] == ttt_list[each[1]] == ttt_list[each[2]] == '0':
            win = 1
    return win


tic_tac_toe = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player01 = input('Введите имя игрока: ')
player02 = 'Бот'
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
        print()
        print('Бот ходит так:')
        tic_tac_toe = BotStep(tic_tac_toe, step_count)
        turn = 1
    PrintTable(tic_tac_toe)
    win = IfWin(tic_tac_toe)
    step_count += 1

if turn == 1 and win == 1:
    print(f'{player02} выиграл! Не плачьте, {player01}, вы проиграли!')
elif turn == 2 and win == 1:
    print(f'{player01} ура! Вы выиграли!')
else:
    print('Игра закончилась ничьей!')



