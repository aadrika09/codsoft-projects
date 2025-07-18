import random 
print("Hello Welcome to Rock paper and scissors Game!\n please enter your choice to Start the game")     

while True:
    user_choice=int(input("Enter your choice: type 0 for Rock for Rock type 1 for paper and type 2 for scissors : "))
    computers_choice=random.randint(0,2)
    print("COMPUTERS CHOICE: {}".format(computers_choice))

    if computers_choice == user_choice:
        print("Its a Draw , please chose again!")


    elif computers_choice == 0 and user_choice == 1:
        print("You Win!!")

    elif computers_choice == 2 and user_choice == 0:
        print("You Win!!")

    elif computers_choice == 2 and user_choice == 1:
        print("You Win!!")

    else: 
        print("You Lose!!")

    ch=input("DO YOU WAN T TO PLAY AGAIN --> \n CLICK Y FOR YES:  \n CLICK N FOR NO: ")
    if ch=='n':
        print("THANK YOU FOR PLAYING!")
        break