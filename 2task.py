# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random


# player1=str(input("Введите имя первого игрока: "))
# player2=str(input("Введите имя второго игрока: "))
# total_candy=int(input("Сколько всего конфет? ")) 

# # how_many_candy=int(input("Возьмите от 1 до 3 конфет: "))
# def random_player():
#     i=random.randint(0,1)    
#     if i == 1:
#         print(f"Первый ход у игрока ", player1)
#     else:
#         print(f"Первый ход у игрока ", player2)
#         player1,player2=player2,player1        
# random_player()

# while total_candy>=3:
#     print("Конфеты тянет ", player1)
#     player1_take=int(input("Сколько возьмешь конфет (от 1 до 3): "))
#     if player1_take > 3 or player1_take <1:
#         print("Только от 1 до 3!")

import random

player1=str(input("Введите имя первого игрока: "))
player2=str(input("Введите имя второго игрока: "))
total_candy=int(input("Сколько всего конфет? ")) 

i=random.randint(0,1)    
if i == 1:
    print(f"Первый ход у игрока ", player1)
else:
    print(f"Первый ход у игрока ", player2)
    player1,player2=player2,player1

while total_candy>=3:
    print("Конфеты тянет ", player1)
    player1_take=int(input("Сколько возьмешь конфет (от 1 до 3): "))
    if player1_take > 3 or player1_take <1:
        print("Только от 1 до 3!")
    else:
        total_candy-=player1_take
        print("Осталось на столе", total_candy)
        if total_candy<=1:
            print("Игрок 1 проиграл")
            break  
        print("Конфеты тянет ", player2)
        player2_take=int(input("Сколько возьмешь конфет (от 1 до 3): "))
        if player2_take > 3 or player2_take <1:
            print("Только от 1 до 3!")           
        else:
            total_candy-=player2_take
            print("Осталось на столе", total_candy)
            if total_candy<=1:
                print("Игрок 2 проиграл")
                break  
