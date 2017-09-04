import random
print("    Welcome to my game")
print("-------Instruction-----------")
print("-----------------------------")
print("(1)Type: Yes to start a game")
print("(2)Type: Quit | Exit if you want to quit the game")
print("(3)Type: Yes to continue the game")

limitNumber = range(1,7)
stringYes = ["Yes","yes","YES"]
while True:
    usrInput = input("Do you want to start: ")
    if usrInput not in stringYes:
        break
    else:
        {
       print("you roll",random.randint(1,6))
    }
    usrInput = input("Do you want to cont: ")
    if usrInput not in stringYes:
        break
    else:
        {
            print("you roll", random.randint(1, 6))
        }

