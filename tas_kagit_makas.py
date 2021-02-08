'''
Developer: Ömer ULUTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program is a Stone-Paper-Scissor Game.
The program takes the choices of the two players in turn as Stone, Paper or Scissor.
And than program calculate that who is win and lose in every game.
This process repeats 10 times. The winner is the one who wins the most games.
'''
i=1
score1=0
score2=0
print("Taş Kağıt Makas Oyununa Hoş Geldiniz")
name1= input("Lütfen 1. oyuncunun ismini yazınız...").upper()
name2= input("Lütfen 2. oyuncunun ismini yazınız...").upper()

while i<3:


    choise1 = input(name1+ ":    Taş, Kağıt, Makas?").lower()
    choise2 = input(name2+ ":    Taş, Kağıt, Makas?").lower()
    
    if choise1 == choise2:
        score1 += 1
        score2 += 1
        i += 1
        print(f"Berabere!\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
    elif choise1 == "taş":
        if choise2 == "kağıt":
            score2 += 1
            i += 1
            print(f"{name2} Kazandı! {choise2} {choise1}ı sarar\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
        else:
            score1 += 1
            i += 1
            print(f"{name1}, Kazandı! {choise1} {choise2}ı kırar\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
    elif choise1 == "kağıt":
        if choise2 == "makas":
            score2 += 1
            i += 1
            print(f"{name2} Kazandı! {choise2} {choise1}ı keser\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
        else:
            score1 += 1
            i += 1
            print(f"{name2} Kazandı! {choise2} {choise1}ı sarar\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
    elif choise1 == "makas":
        if choise2 == "taş":
            score2 += 1
            i += 1
            print(f"{name2} Kazandı! {choise2} {choise1}ı kırar\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
        else:
            score1 += 1
            i += 1
            print(f"{name1}, Kazandı! {choise1} {choise2}ı keser\n Skorlar ==>>    {name1}: {score1},  {name2}: {score2}")
    else:
        print("Oyuna başlamak için geçerli bir kelime girmediniz!!!")