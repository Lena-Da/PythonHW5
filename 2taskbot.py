import random

player1=str(input("Введите имя первого игрока: "))
print("Второй игрок: ")
player2=print("Компьютер")
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
        print("Конфеты тянет компьютер")
        player2_take=random.randint(1,3)
        print("Компьютер взял: ", player2_take)
        total_candy-=player2_take
        print("Осталось на столе", total_candy)
        if total_candy<=1:
            print("Компьютер проиграл")
            break  

