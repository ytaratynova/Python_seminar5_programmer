# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
#
# Здесь реализована игра с не очень умным ботом. Количество конфет он выбирает радомно.

from random import randint 

def PlayerTurn(player, num_of_can):
    i_take = int(input(f'{player}! Введите количество конфет, которое хотите взять (не более 28 штук):'))
    while i_take > 28 or i_take < 1 or i_take > num_of_can:
        i_take = int(input('Некорректное поведение! Введите количество конфет, которое хотите взять (не более 28 штук и не больше остатка):'))
    print()
    return i_take

def BotTurn(num_of_can):
    if num_of_can < 28:
          bot_took = num_of_can
    else:
        bot_took = randint(1, 28)
    return bot_took

def PrintTurnInfo(player, took, num_of_can):
    print(f'{player} взял {took} конфет. Теперь на столе осталось {num_of_can} конфет.')
    print()


player01 = input('Введите имя игрока: ')
player02 = 'Бот'
print()

number_of_candies = 2021

turn = randint(1, 2)
if turn == 1:
    print(f"Первый ход определен жеребьевкой: ходит {player01}!")
else:
    print(f"Первый ход определен жеребьевкой: ходит {player02}!")
print()


while number_of_candies > 0:
    print(f'В куче {number_of_candies} конфет!')
    if turn == 1:
       took = PlayerTurn(player01, number_of_candies)
       number_of_candies -= took
       turn = 2
       PrintTurnInfo(player01, took, number_of_candies)
    else:
        took = BotTurn(number_of_candies)
        turn = 1
        number_of_candies -= took
        PrintTurnInfo(player02, took, number_of_candies)
    

if turn == 1:
    print(f'{player02}, ура! Вы выиграли! Все конфеты ваши! {player01}, отдайте свои конфеты!')
else:
    print(f'{player01}, ура! Вы выиграли! Все конфеты ваши! {player02}, отдайте свои конфеты!')