import random
def game(computer, player):
    if computer==player:
        return None
    elif computer =='snake':
        if player=='water' or player=='Water':
            return False
        elif player=='gun' or player=='Gun':
            return True
    elif computer=='water':
        if player=='gun' or player=='Gun':
            return False
        elif player=='snake' or player=='Snake':
            return True
    elif computer=='gun':
        if player=='snake' or player=='Snake':
            return False
        elif player=='water' or player=='Water':
            return True

print(" Computer Turn:\nSanke\nWater\nGun:\n ")
randno=random.randint(1,3)
if randno==1:
    computer='snake'
elif randno==2:
    computer='water'
else:
    computer='gun'


        
print(" Your Turn:\nSanke\nWater\nGun: ")
player=input(" Enter Snake Water or Gun to play the game: ")
a=game( computer,player)

if player=="Snake" or player=="snake" or player=="Water" or player=='water' or player=='gun' or player=="Gun":
    print(f" Computer choose {computer}")
    print(f" You choose {player}")

    if a==None:
        print(" Your and your's Computer's choice is same")
    elif a:
        print(" Congratulations! You Won!!!")
    else:
        print(" Alas! You lose")
else:
    raise SyntaxWarning
