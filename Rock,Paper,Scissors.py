import random 

while True:
    rounds=int(input("How many rounds do you want to play? "))
    choices=["rock","paper","scissors"]
    userscore=0
    computerscore=0
    for i in range(rounds):
            user=input("Enter your choice (rock, paper, scissors): ").lower()
            computer=random.choice(choices)
            print("You chose:", user)
            print("Computer chose:", computer)

            if user==computer:
                   print("It's a tie!")
            elif(user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
                   print("You win!")
                   userscore+=1
            else:
                   print("Computer wins!")
                   computerscore+=1

    print("Final Score:")
    print("You:", userscore)
    print("Computer:", computerscore)

    if userscore==computerscore:
        print("The game is a tie!")
    elif userscore>computerscore:
        print("You are the overall winner!")
    else:
        print("Computer is the overall winner!")        