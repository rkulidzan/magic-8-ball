import random
import time, sys
play_again = 'yes'

while play_again == 'yes':
    str(input("Welcome to the Magic 8-Ball. Enter your question: ")).lower()
    
#Delay output for 1 second each
    print("Thinking...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()

#Generate a random integer/response
    response = random.randint(0,8)
    
    if response == 1:
        print("LOL. No chance!")
    elif response == 2:
        print("Maybe. See how I feel later")
    elif response == 3:
        print("Ask Ricky.")
    elif response == 4:
        print("Sure!")
    elif response == 5:
        print("Mmmmm K, weird question.")
    elif response == 6:
        print("Nah.")
    elif response == 7:
        print("You go Glen Coco!")
    elif response == 8:
        print("I always knew you were a winner.")
    else:
        print("Invalid question. Try again!")

    play_again = str(input("Would you like to ask another question? yes/no/enter ")).lower()
    if play_again == 'no':
        print("Goodbye! Thanks for playing!")
        sys.exit()
    elif: play_again == "":
        sys.exit()