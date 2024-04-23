import random
restart=True
def stone():
    print("Stone Paper Scissors!\n")
    print("Choose the number coressponding to the gestures\n1 - Stone\n2 - Paper\n3 - Scissor\n")
    user_choice=int(input("Your choice : "))
    random_choice=random.randint(1,3)
    if user_choice==1:
        print("You chose : Stone")
    elif user_choice==2:
        print("You Chose : Paper")
    else:
        print("You chose : Scissor")
    if random_choice==1:
        print("Computer chose : Stone")
    elif random_choice==2:
        print("Computer Chose : Paper")
    else:
        print("Computer chose : Scissor")
    if user_choice==random_choice:
        print("IT'S A DRAW!")
    elif user_choice==1 and random_choice==2:
        print("THE COMPUTER WON!")
    elif user_choice==1 and random_choice==3:
        print("YOU WON!")
    elif user_choice==2 and random_choice==3:
        print("THE COMPUTER WON!")
    elif user_choice==2 and random_choice==1:
        print("YOU WON!")
    elif user_choice==3 and random_choice==1:
        print("THE COMPUTER WON!")
    else:
        print("YOU WON")
    want_restart=input("Do you want to play again? : ")
    if want_restart.lower()=="no":
        return 0
    return stone()
stone()
