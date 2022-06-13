import random
userName = input("input your preferred username: ")

while True:
   
    choiceDict = {"R":"Rock", "P":"Paper", "S":"Scissors"}

    plausibleOptions = ["R","P","S"]
    
    userChoice = input("R => Rock; P => Paper; S => Scissors \n Kindly pick one: ").upper()

    computerChoice = random.choice(plausibleOptions)
    if userChoice in plausibleOptions:

        if userChoice == computerChoice:
            print(f"Player ({choiceDict[userChoice]}) : CPU ({choiceDict[computerChoice]})")
            print("It is a tie!")
            continue
        elif userChoice == "R" and computerChoice == "S" or userChoice =="P" and computerChoice =="R" or userChoice =="S" and computerChoice =="P":
            print(f"Player ({choiceDict[userChoice]}) : CPU ({choiceDict[computerChoice]})")
            print(f"{userName} wins!")
            break
        else:
            print(f"Player ({choiceDict[userChoice]}) : CPU ({choiceDict[computerChoice]})")
            print(f"CPU wins!")
            break
    else:
        print("Error! you chose outside the stipulated options! \n Try again xoxo")
        continue