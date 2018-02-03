import sys
import random

ans = True

while ans:
    question = input("ask me a question: ")
    answers = random.randint(1,8)

    if question == "":
        sys.exit()
    elif answers == 1:
        print ("I see good things")
    elif answers == 2:
        print("Its uncertain")
    elif answers == 3:
        print("Ask me again later")
    elif answers == 4:
        print("You should do it!")
    elif answers == 5:
        print("DANGER WILL ROBINSON")
    elif answers == 6:
        print("Do, or do not. There is no try")
    elif answers == 7:
        print("Use the force Luke")
    elif answers == 8:
        print("Take me home, country road")
