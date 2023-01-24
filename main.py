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
    lives = 5
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
    if PentajackGame.gameWin == False:
        print("""You find yourself as a Casino, bustling with gamblers at nearly every slot and table. You try to
        start conversation to try and fin out if anyone knows what is going on or how to escape, but they are completely
        entranced in their gambling activities. You try and leave the room from where you came from, however, you soon
        realise that the entrance that you entered through has now mysteriously vanished.
        """)
        print("""You notice a hooded figure cloaked in black, staring a you. They eventually approach you and say that
        they overheard you. "There's one way you can leave this place" he says, as he leads you to a table. "All you 
        have to do is beat me in a game of Pentajack. The rules are simple; score higher than me, but don't go over 21.
        In this game, you don't play with chips; you play with your life.
        """)
        print("""Completely mortified, you freeze in place. After a moment, you regain composure and soon realise that
        a better option is truly wishful thinking and that this is the only way forward and out. You accept the rules
        of the game. The figure offers you a seat.
        """)
        print("Welcome to the table")
    else:
        print("You've already been in this room.")
        return
    while True:
        draw()
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

class Combat:
    gameWin = False
    roundNumber = 0
    weapons = ["Sword", "Lance", "Axe"]
    element = ["Fire", "Water", "Ice"]
    playerAttack = 0
    playerHP = 100
    playerWeapon = {}
    playerElement = {}
    enemyAttack = 0
    enemyHP = 100
    enemyWeapon = None
    enemyElement = None
def enemyChoice():
    Combat.enemyWeapon = random.choice(Combat.weapons)
    print(Combat.enemyWeapon)
    Combat.enemyElement = random.choice(Combat.element)
    print((Combat.enemyElement))
    if "Ice" in Combat.enemyElement:
        print("""There is a misty atmosphere swirling around the arena...""")
    elif "Fire" in Combat.enemyElement:
        print("""You feel as though the arena is the Sahara Desert, as you wipe the sweat off your brow...""")
    elif "Water" in Combat.enemyElement:
        print("""You feel your shoes slightly sink into the ground as the floor in the arena dampens a bit...""")
def playerChoice():
    while True:
        weaponChoice = input("Select a weapon. You have a sword, a lance and an axe.")
        if weaponChoice.lower() == "sword":
            Combat.playerWeapon = {"Sword": 10}
            break
        elif weaponChoice.lower() == "lance":
            Combat.playerWeapon = {"Lance": 10}
            break
        elif weaponChoice.lower() == "axe":
            Combat.playerWeapon = {"Axe": 10}
            break
        else:
            print("You don't have that weapon. Are you trying to die?!")
            continue
    while True:
        elementChoice = input("Select the magic you will use. You can use fire, water or ice.")
        if elementChoice.lower() == "fire":
            Combat.playerElement = {"Fire": 10}
            break
        elif elementChoice.lower() == "water":
            Combat.playerElement = {"Water": 10}
            break
        elif elementChoice.lower() == "ice":
            Combat.playerElement = {"Ice": 10}
            break
        else:
            print("You don't know how to cast that type of magic. Stop fooling around!")
            continue
def damage():
    if "Sword" in Combat.playerWeapon and "Axe" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5

    elif "Sword" in Combat.playerWeapon and "Lance" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20

    elif "Lance" in Combat.playerWeapon and "Sword" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5

    elif "Lance" in Combat.playerWeapon and "Axe" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20

    elif "Axe" in Combat.playerWeapon and "Lance" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5

    elif "Axe" in Combat.playerWeapon and "Sword" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20
    else:
        Combat.playerAttack = 10
        Combat.enemyAttack = 10

    if "Fire" in Combat.playerElement and "Ice" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20

    elif "Fire" in Combat.playerElement and "Water" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20

    elif "Water" in Combat.playerElement and "Fire" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20

    elif "Water" in Combat.playerElement and "Ice" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20

    elif "Ice" in Combat.playerElement and "Water" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20

    elif "Ice" in Combat.playerElement and "Fire" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20

    else:
        Combat.playerAttack = Combat.playerAttack + 5
        Combat.enemyAttack = Combat.enemyAttack + 5



def gameFramework():
    if Combat.gameWin == False:
        print("Hello")
    else:
        print("Goodbye")
    while True:
        if Combat.gameWin == False:
            enemyChoice()
            playerChoice()
            damage()
        else:
            print("You've already been in this room.")
            break


nextStage = False

while nextStage == False:
    #gameFramework()
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