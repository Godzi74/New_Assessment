import random

def room1():
    safe_code = []
    while len(safe_code) < 3:
        code = random.randint(3, 12)
        if code not in safe_code:
            safe_code.append(code)

    codes_cracked = 0
    attemptsMade = 0
    print("You enter an empty room with nothing but a table and a safe.")
    while codes_cracked < 3 and attemptsMade < 3:
        for x in safe_code:
            print("The code is", x)
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if num2 == 1:
                    raise ValueError("You can't pick one for the second number")
                    break
                if num1 / num2 == x:
                    print("Code cracked")
                    codes_cracked = codes_cracked + 1
                if num1 / num2 != x:
                    print("Incorrect code")
                    attemptsMade = attemptsMade + 1
            except ValueError:
                print("That is not a number")
                break

    if codes_cracked >= 3 and attemptsMade < 3:
        print("Safe opened")
        return
    else:
        print("L.")
        exit()

class PentajackGame:

    playing = True
    playerHand = []
    playerTotal = 0
    lives = 1
    dealerHand = []
    dealerTotal = 0
    gameWin = False


def draw():
    PentajackGame.playerHand.append(random.randint(1,10))
    PentajackGame.playerHand.append(random.randint(1,10))
    PentajackGame.playerTotal = sum(PentajackGame.playerHand)
    PentajackGame.dealerHand.append(random.randint(1, 10))
    PentajackGame.dealerTotal = sum(PentajackGame.dealerHand)
    print("""You have a {} and a {}. Your total is {} The dealer has a {}.""".format(PentajackGame.playerHand[0], PentajackGame.playerHand[1], PentajackGame.playerTotal, PentajackGame.dealerHand[0]))


def hit():
    PentajackGame.playerHand.append((random.randint(1, 10)))
    PentajackGame.playerTotal = sum(PentajackGame.playerHand)
    print(PentajackGame.playerTotal)


def dealerHit():
    PentajackGame.dealerHand.append(random.randint(1, 10))
    PentajackGame.dealerTotal = sum(PentajackGame.dealerHand)


def hitOrStand():
    global playing

    while True:
        userAnswer = input("Would you like to hit or stand?")
        if userAnswer.lower() == "hit":
            hit()
        elif userAnswer.lower() == "stand":
            print("You have stood your ground. The dealer is now playing.")
            PentajackGame.playing = False
        else:
            print("That's not an answer. Give me a real man's answer.")
            continue
        break


def push():
    print("The dealer drew {}. You also have {}. No winners!".format(PentajackGame.dealerTotal, PentajackGame.playerTotal))

def Pentajack():
    while True:
        if PentajackGame.gameWin == False:
            print("Welcome to the table")
            draw()
        else:
            print("You've already been in this room.")
            break
        while PentajackGame.playing:
            hitOrStand()

            if PentajackGame.playerTotal > 21:
                print("You busted!")
                PentajackGame.lives = PentajackGame.lives - 1
                print("You lost 1 life. You have {} remaining.".format(PentajackGame.lives))
                break
        if PentajackGame.playerTotal <= 21:
            while PentajackGame.dealerTotal < 17:
                dealerHit()
            if PentajackGame.dealerTotal > 21:
                print("The dealer drew {}. The dealer went bust!".format(PentajackGame.dealerTotal))
                print("""You won against the dealer! """)
                print("""The dealer draws one more card and gives it to you. On the back of the card, "2. E" is written in
                blood. You stash the card away in your clues inventory.""")
                PentajackGame.gameWin = True
            elif PentajackGame.dealerTotal > PentajackGame.playerTotal:
                print("The dealer drew {}. You lost against the dealer.".format(PentajackGame.dealerTotal))
                PentajackGame.lives = PentajackGame.lives - 1
                print("You lost 1 life. You have {} remaining.".format(PentajackGame.lives))
            elif PentajackGame.dealerTotal < PentajackGame.playerTotal:
                print("The dealer drew {}. You have a higher hand of {}".format(PentajackGame.dealerTotal,
                                                                                PentajackGame.playerTotal))
                print("""You won against the dealer! """)
                print("""The dealer draws one more card and gives it to you. On the back of the card, "2. E" is written in
                            blood. You stash the card away in your clues inventory.""")
                PentajackGame.gameWin = True
            else:
                push()

        if PentajackGame.gameWin == False and PentajackGame.lives > 0:
            PentajackGame.playing = True
            print("""You ask for another hand.""")
            PentajackGame.playerHand.clear()
            PentajackGame.dealerHand.clear()
            PentajackGame.playerTotal = 0
            PentajackGame.dealerTotal = 0
            continue
        elif PentajackGame.gameWin == False and PentajackGame.lives == 0:
            print("""You lean back from the table in horror, as you have no more lives to gamble. You slowly slump over in
            your chair as you feel your life force seep away from you.""")
            exit()

        else:
            print("You walk away from the table, winnings in hand as the exit to the room opens up once more.")
            break
nextStage = False

while nextStage == False:
    gameStart = input("""You awake from a deep sleep and find yourself in a barren, pentagon shaped room. There is 
    a door on each wall of the room, including a large steel door labeled 'E' with a four code lock. On this door, there
     is a small note that reads: 'Forfeit your life, or challenge the Pentagon'. Do you accept the challenge? """)

    try:

        if gameStart.lower() in ["y", "yes"]:
            print("""With not many other options, you yell at the top of your lungs that you accept this challenge.
            Suddenly, your hear four the sound of four locks unlocking. Aside from the large metal door, you realise
            that the other doors are unlocked, labeled from A to D.""")
            nextStage = True

        elif gameStart.lower() in ["n", "no"]:
            print("""With how incredibly silly this situation is, you simply tear up the note and begin looking for
            alternate escape routes. Soon after, the ground begins to quake and a hole slowly begins to extend to the
            edges of the room. With nowhere to run, you wait for your inevitable demise, as you finally sink into
            the hole; the deep dark abyss, where your tale ends...""")
            nextStage = False
            break

        else:
            raise ValueError("I can't have that as an answer!")
    except :
            print("I can't have that as an answer!")
            nextStage = False

while nextStage == True:
    doorChoice = input("Which door will you check?")
    try:
        if doorChoice.lower() == "a":
            Pentajack()
        elif doorChoice.lower() == "b":
            room1()
        else:
            raise ValueError("I can't have that as an answer!")
    except:
        print("I can't have that as an answer!")