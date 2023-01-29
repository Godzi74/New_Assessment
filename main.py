import random
import time
# clues list that contains each clue that the player has obtained from each door. This is printed when the player approaches the final door.
clues = []

# code cracker game.

class Codecracking:
    safe_code = []
    gameWin = False
    codes_cracked = 0
    attemptsMade = 0
def codeCracker():
    # randomises safe code
    while len(Codecracking.safe_code) < 3:
        code = random.randint(3, 12)
        if code not in Codecracking.safe_code:
            Codecracking.safe_code.append(code)



# checks if the player has already been in the room.
    if Codecracking.gameWin == False:
        print("""You enter an empty room with nothing but a table and a safe. Upon approaching the table, you realise 
that the safe has the letter "X" written all over it. The walls are also engraved all over with a peculiar equation:
"x = 1st / 2nd". 
You touch the safe's screen and a robotic voice begins to play. "Welcome to the safe. Please enter the correct code. 
Intruders will be punished with their lives." Prioritising your life above all, you turn away from the table and head
back to where you came from, however you realise that the door has been completely shut behind you. In hopes of freedom
from this room, you go back to the safe.
""")
    else:
        print("You've already been in this room.")
        return

    # allows the player to play as long as they haven't met the win/lose condition
    while Codecracking.codes_cracked < 3 and Codecracking.attemptsMade < 3:
        for x in Codecracking.safe_code:
            print("The code is", x)
            # asks the player for two values
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if num2 == 1:
                    raise ValueError("You can't pick one for the second number")

            # equation to check whether the input matches the code.
            # outcome when the code matches
                if num1 / num2 == x:
                    print("Code cracked")
                    Codecracking.codes_cracked = Codecracking.codes_cracked + 1
            # outcome when the code doesn't match
                if num1 / num2 != x:
                    print("Incorrect code.")
                    print("""You notice the walls closing in on themselves, which is accompanied by a rumbling"
noise.
""")

                    Codecracking.attemptsMade = Codecracking.attemptsMade + 1
            # error handling
            except ValueError:
                print("That is not a number")
                print("""You notice the walls closing in on themselves, which is accompanied by a rumbling"
noise.
""")
                Codecracking.attemptsMade = Codecracking.attemptsMade + 1


            # when win condition is reached
    if Codecracking.codes_cracked >= 3 and Codecracking.attemptsMade < 3:
        print("""The safe suddenly begins to flash, then glows a solid green colour. "Code cracking completed" the voice
says. "Safe opened." Fantasising about what treasures the safe beholds, you peer into the safe. In it, holds only a
sheet of paper that has "4: R" written on it. A door leading back to the lobby opens. With disappointment written all
over you face, you leave the room.
""")
        clues.append("4. R")
        Codecracking.gameWin = True
        return
    else:
        # when lose condition is reached.
        print("""The safe suddenly begins to flash a bright red colour. "Code cracking failed. Intruder detected!
initiating anti-theft protocols". The walls completely close in on itself. What a horrific end!
""")
        time.sleep(7)
        exit()

# the class and methods for the Pentajack room.
class PentajackGame:

    playing = True
    playerHand = []
    playerTotal = 0
    lives = 5
    dealerHand = []
    dealerTotal = 0
    gameWin = False


# gives the player and the dealer a random set of cards at the start of each game.
def draw():
    PentajackGame.playerHand.append(random.randint(1,10))
    PentajackGame.playerHand.append(random.randint(1,10))
    PentajackGame.playerTotal = sum(PentajackGame.playerHand)
    PentajackGame.dealerHand.append(random.randint(1, 10))
    PentajackGame.dealerTotal = sum(PentajackGame.dealerHand)
    print("""You have a {} and a {}. Your total is {} The dealer has a {}.""".format(PentajackGame.playerHand[0], PentajackGame.playerHand[1], PentajackGame.playerTotal, PentajackGame.dealerHand[0]))

# allows the player to draw another card.
def hit():
    PentajackGame.playerHand.append((random.randint(1, 10)))
    PentajackGame.playerTotal = sum(PentajackGame.playerHand)
    print(PentajackGame.playerTotal)

# makes the dealer draw a card
def dealerHit():
    PentajackGame.dealerHand.append(random.randint(1, 10))
    PentajackGame.dealerTotal = sum(PentajackGame.dealerHand)

# asks the player whether they want to continue drawing cards or stop.
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

        # is called when the player and the dealer has the same hand. This is a draw state.
def push():
    print("The dealer drew {}. You also have {}. No winners!".format(PentajackGame.dealerTotal, PentajackGame.playerTotal))

    # the main game method. Calls other methods when certain conditions are met.
def Pentajack():
    if PentajackGame.gameWin == False:
        print("""You find yourself as a Casino, bustling with gamblers at nearly every slot and table. You try to
start conversation to try and find out if anyone knows what is going on or how to escape, but they are 
completely entranced in their gambling activities. You try and leave the room from where you came from, however, you 
soon realise that the entrance that you entered through has now mysteriously vanished.
""")

        print("""You notice a hooded figure cloaked in black, staring at you. They eventually approach you and say that
they overheard you. "There's one way you can leave this place" he says, as he leads you to a table. "All you 
have to do is beat me in a game of Pentajack. The rules are simple; score higher than me, but don't go over 21.
In this game, you don't play with chips; you play with your life." 
""")

        print("""Completely mortified, you freeze in place. After a moment, you regain composure and soon realise that
a better option is truly wishful thinking and that this is the only way forward and out. You accept the rules
of the game. The figure offers you a seat.
""")

        print("Welcome to the table")
    else:
        # returns the player to the main room if they have already entered the room.
        print("You've already been in this room.")
        return
    while True:
        draw()
        while PentajackGame.playing:
            hitOrStand()
            # when player has over 21, the player loses.
            if PentajackGame.playerTotal > 21:
                print("You busted!")
                PentajackGame.lives = PentajackGame.lives - 1
                print("You lost 1 life. You have {} remaining.".format(PentajackGame.lives))
                break
        if PentajackGame.playerTotal <= 21:
            # when the player has less than 21 and stops drawing, the dealer draws.
            while PentajackGame.dealerTotal < 17:
                dealerHit()
            # when the dealer has less than the player, the player wins.
            if PentajackGame.dealerTotal > 21:
                print("The dealer drew {}. The dealer went bust!".format(PentajackGame.dealerTotal))
                print("""You won against the dealer! """)
                print("""The dealer draws one more card and gives it to you. On the back of the card, "2. E" is written in
                blood. You stash the card away in your clues inventory.
                """)
                clues.append("2. E")
                PentajackGame.gameWin = True
            elif PentajackGame.dealerTotal > PentajackGame.playerTotal:
                # when the dealer has more than the player, they lose.
                print("The dealer drew {}. You lost against the dealer.".format(PentajackGame.dealerTotal))
                PentajackGame.lives = PentajackGame.lives - 1
                print("You lost 1 life. You have {} remaining.".format(PentajackGame.lives))
            elif PentajackGame.dealerTotal < PentajackGame.playerTotal:
                # when the player has more than the dealer they win.
                print("The dealer drew {}. You have a higher hand of {}".format(PentajackGame.dealerTotal,
                                                                                PentajackGame.playerTotal))
                print("""You won against the dealer! """)
                print("""The dealer draws one more card and gives it to you. On the back of the card, "2. E" is written 
                        in blood. You stash the card away in your clues inventory.
                        """)
                clues.append("2. E")
                PentajackGame.gameWin = True
            else:
                push()

        # allows the player to continue playing as long as they have lives.
        if PentajackGame.gameWin == False and PentajackGame.lives > 0:
            PentajackGame.playing = True
            print("""You ask for another hand.""")
            PentajackGame.playerHand.clear()
            PentajackGame.dealerHand.clear()
            PentajackGame.playerTotal = 0
            PentajackGame.dealerTotal = 0
            continue

        # when the player runs out of lives, they lose.
        elif PentajackGame.gameWin == False and PentajackGame.lives == 0:
            print("""You lean back from the table in horror, as you have no more lives to gamble. You slowly slump over 
in your chair as you feel your life force seep away from you.""")
            time.sleep(7)
            exit()

        else:
            print("You walk away from the table, winnings in hand as the exit to the room opens up once more.")
            break


# class and methods for the unscramble game.
class Unscramble:
    gameWin = False
    lives = 4
    words = ["you", "shall", "never", "escape"]
    wordsCorrect = 0
    answer = None

# prints out the word that the player must unscramble based on how many words they have completed.
# when they guess incorrectly, they lose a life.
def wordPicker():
    while Unscramble.lives > 0 and Unscramble.wordsCorrect < 4 and Unscramble.wordsCorrect == 0:
        print("Your first word is ""Oyu"". ")
        Unscramble.answer = input()
        if Unscramble.answer.lower() == Unscramble.words[0]:
            print("Word successfully unscrambled.")
            Unscramble.wordsCorrect = Unscramble.wordsCorrect + 1
            Unscramble.lives = 4
            print("The room's water level sinks back to the ground floor.")
            print("Your lives refreshed!")
        else:
            print("A loud noise and flashing red lights fill the room. The level of water in the room increases.")
            Unscramble.lives = Unscramble.lives - 1
            if Unscramble.lives == 1:
                print("You have {} life remaining.".format(Unscramble.lives))
            else:
                print("You have {} lives remaining.".format(Unscramble.lives))
        continue

    while Unscramble.lives > 0 and Unscramble.wordsCorrect < 4 and Unscramble.wordsCorrect == 1:
        print("Your second word is ""Hlsla""")
        Unscramble.answer = input()
        if Unscramble.answer.lower() == Unscramble.words[1]:
            print("Word successfully unscrambled.")
            Unscramble.wordsCorrect = Unscramble.wordsCorrect + 1
            Unscramble.lives = 4
            print("The room's water level sinks back to the ground floor.")
            print("Your lives refreshed!")
        else:
            print("A loud noise and flashing red lights fill the room. The level of water in the room increases.")
            Unscramble.lives = Unscramble.lives - 1
            if Unscramble.lives == 1:
                print("You have {} life remaining.".format(Unscramble.lives))
            else:
                print("You have {} lives remaining.".format(Unscramble.lives))
        continue

    while Unscramble.lives > 0 and Unscramble.wordsCorrect < 4 and Unscramble.wordsCorrect == 2:
        print("Your second word is ""Enrve""")
        Unscramble.answer = input()
        if Unscramble.answer.lower() == Unscramble.words[2]:
            print("Word successfully unscrambled.")
            Unscramble.wordsCorrect = Unscramble.wordsCorrect + 1
            Unscramble.lives = 4
            print("The room's water level sinks back to the ground floor.")
            print("Your lives refreshed!")
        else:
            print("A loud noise and flashing red lights fill the room. The level of water in the room increases.")
            Unscramble.lives = Unscramble.lives - 1
            if Unscramble.lives == 1:
                print("You have {} life remaining.".format(Unscramble.lives))
            else:
                print("You have {} lives remaining.".format(Unscramble.lives))
        continue

    while Unscramble.lives > 0 and Unscramble.wordsCorrect < 4 and Unscramble.wordsCorrect == 3:
        print("Your second word is ""Peeacs""")
        Unscramble.answer = input()
        if Unscramble.answer == Unscramble.words[3]:
            print("Word successfully unscrambled.")
            Unscramble.wordsCorrect = Unscramble.wordsCorrect + 1
            Unscramble.lives = 4
            print("The room's water level sinks back to the ground floor.")
            print("Your lives refreshed!")
        else:
            print("A loud noise and flashing red lights fill the room. The level of water in the room increases.")
            Unscramble.lives = Unscramble.lives - 1
            # informs the user on how many lives they have left.
            if Unscramble.lives == 1:
                print("You have {} life remaining.".format(Unscramble.lives))
            else:
                print("You have {} lives remaining.".format(Unscramble.lives))
        continue

# method that plays out the game and its outcomes.
def mainUnscramble():
    if Unscramble.gameWin == False:
        print("""You enter a room, filled with terminals and screens labelled all over with 1s and 0s. In the centre of
the room lies a tablet with four different codes that need to be decrypted. The door behind you suddenly closes as you 
touch the tablet. You also notice a shallow pool of water on the ground. With nothing much else to do, you try and
decipher the codes.""")
    else:
        # returns the player if they have already completed the room.
        print("You've already been in this room.")
        return
    while True:
        wordPicker()
        # player wins when they decipher all words,
        if Unscramble.lives > 0 and Unscramble.wordsCorrect >= 4:
            print("""The tablet changes to a white screen that reads: "deciphering complete. Draining water and opening
exit." The screen then goes blank, before displaying "3. A" in red text. You make a note of this before leaving the room.
""")
            Unscramble.gameWin = True
            clues.append("3. A")
            return
        # player loses when they run out of lives.
        elif Unscramble.lives <= 0 and Unscramble.wordsCorrect < 4:
            print("""With the final failed attempt, the room fills with water again, filling in the last air pocket. You
are completely submerged in water...
""")
            time.sleep(7)
            exit()
            break

# class and methods for Combat simulator
class Combat:
    gameWin = False
    roundNumber = 1
    weapons = ["Sword", "Lance", "Axe"]
    element = ["Fire", "Water", "Ice"]
    playerAttack = 0
    playerHP = 150
    playerWeapon = {}
    playerElement = {}
    enemyAttack = 0
    enemyHP = 150
    enemyWeapon = None
    enemyElement = None
def enemyChoice():
    # chooses a random weapon and element from the list of available ones.
    Combat.enemyWeapon = random.choice(Combat.weapons)
    Combat.enemyElement = random.choice(Combat.element)
    # prints out the round number and hints to the player what the enemy is using.
    print("Round {}. FIGHT!".format(Combat.roundNumber))
    if "Ice" in Combat.enemyElement:
        print("""There is a misty atmosphere swirling around the arena...""")
    elif "Fire" in Combat.enemyElement:
        print("""You feel as though the arena is the Sahara Desert, as you wipe the sweat off your brow...""")
    elif "Water" in Combat.enemyElement:
        print("""You feel your shoes slightly sink into the ground as the floor in the arena dampens a bit...""")
def playerChoice():
    while True:
        # allows the player to choose a weapon.
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
            # error handling.
            print("You don't have that weapon. Are you trying to die?!")
            continue
    while True:
        # allows the player to select an element.
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
            # error handling.
            print("You don't know how to cast that type of magic. Stop fooling around!")
            continue

# calculates the damage outcomes depending on what the player picked vs. what the enemy has.
def fight():
    if "Sword" in Combat.playerWeapon and "Axe" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5
        print("Your sword has an advantage against their axe!")
    elif "Sword" in Combat.playerWeapon and "Lance" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20
        print("Your sword is at a disadvantage to their lance!")
    elif "Lance" in Combat.playerWeapon and "Sword" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5
        print("Your lance has an advantage against their sword!")
    elif "Lance" in Combat.playerWeapon and "Axe" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20
        print("Your lance is at a disadvantage to their axe!")
    elif "Axe" in Combat.playerWeapon and "Lance" in Combat.enemyWeapon:
        Combat.playerAttack = 20
        Combat.enemyAttack = 5
        print("Your axe has an advantage against their lance!")
    elif "Axe" in Combat.playerWeapon and "Sword" in Combat.enemyWeapon:
        Combat.playerAttack = 5
        Combat.enemyAttack = 20
        print("Your axe is at a disadvantage to their sword!")
    else:
        Combat.playerAttack = 10
        Combat.enemyAttack = 10
        print("Your weapons are equally matched!")

    if "Fire" in Combat.playerElement and "Ice" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""Your burning flames melt away your foe's power of ice, rendering them with a normal weapon. You deal {}
                to the enemy. Your foe has {} HP. The enemy deals {} to you. You have {} HP.""".format(Combat.playerAttack,
        Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

    elif "Fire" in Combat.playerElement and "Water" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""Your burning flames are extinguished by your foe's overwhelming torrents, rendering you with a normal 
                weapon. You deal {} to the enemy. Your foe has {} HP. The enemy deals {} to you. You have {} HP.""".format(Combat.playerAttack,
        Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

    elif "Water" in Combat.playerElement and "Fire" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""Your raging tides extinguish the flames of your foe's weapon, rendering them with a normal weapon. You 
                deal {} to the enemy. Your foe has {} HP. The enemy deals {} to you. You have {} HP.""".format(Combat.playerAttack,
        Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))

        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

    elif "Water" in Combat.playerElement and "Ice" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""Your raging tides are frozen to a halt by the frost of your foe's weapon, rendering you with a normal 
                weapon. You deal {} to the enemy. Your foe has {} HP. The enemy deals {} to you. You have {} HP.""".format(
            Combat.playerAttack,
            Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1


    elif "Ice" in Combat.playerElement and "Water" in Combat.enemyElement:
        Combat.playerAttack = Combat.playerAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""The wicked blizzard emerging from your weapon freezes and shatters the waves of your foe's weapon, 
                rendering them with a normal weapon. You deal {} to the enemy. Your foe has {} HP. The enemy deals {} 
                to you. You have {} HP.""".format(
            Combat.playerAttack,
            Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

    elif "Ice" in Combat.playerElement and "Fire" in Combat.enemyElement:
        Combat.enemyAttack = Combat.enemyAttack + 20
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""The wicked blizzard emerging from your weapon dissipates due to the growing flames of your foe's
                weapon, rendering you with a normal weapon. You deal {} to the enemy. Your foe has {} HP. The enemy deals {} 
                to you. You have {} HP.""".format(
            Combat.playerAttack,
            Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

    else:
        Combat.playerAttack = Combat.playerAttack + 5
        Combat.enemyAttack = Combat.enemyAttack + 5
        Combat.playerHP = Combat.playerHP - Combat.enemyAttack
        Combat.enemyHP = Combat.enemyHP - Combat.playerAttack
        print("""The power of both your elements shine as they are both equally matched. You deal {} to the enemy. Your 
foe has {} HP. The enemy deals {} to you. You have {} HP.""".format(
            Combat.playerAttack,
            Combat.enemyHP, Combat.enemyAttack, Combat.playerHP))
        Combat.enemyAttack = 0
        Combat.enemyElement = None
        Combat.enemyWeapon = None
        Combat.roundNumber = Combat.roundNumber + 1

# handles the structure of the game.
def gameFramework():
    # checks if the player has already completed this room.
    if Combat.gameWin == False:
        print("""Upon entering the room, you are surrounded with loud cheering and sand dust clouds that hover along the
ground. You are in a colosseum. Before you awaits a fearsome gladiator that tells you to draw your weapon. To escape
this predicament, you quickly turn around and make a dash for the exit, but you are soon met by two other gladiators
with spears that force you back into the colosseum. "You run from a gladiatorial contest? Fool! Have you no shame?" the
gladiator says mockingly. He kicks a gladiator helm along the ground in your direction. "Steel yourself" he yells, as he
picks his weapon. Trembling, you pick up and wear the helm, preparing for the worst.
""")
    else:
        print("You've already been in this room.")
        return
    while True:
        # allows the fight to continue as long as the player and enemy have remaining hp.
        while Combat.playerHP > 0 and Combat.enemyHP > 0:
            enemyChoice()
            playerChoice()
            fight()

        # win state.
        if Combat.playerHP > 0 and Combat.enemyHP <= 0:
            print("""The gladiator falls. Astonished, the crowd goes completely silent, then a great uproar fills the
colosseum once. A gladiator walks up to you with something in hand. "Please take this as a monument to your strength and
bravery." He hands you a celebratory dagger, with the writing "1. F" engraved on it. You try and ask him if he knows
 anything about escaping the pentagon, but your question is utterly drowned out by the cheers of the crowd. You leave
 the colosseum.
 """)
            clues.append("1. F")
            Combat.gameWin = True
            break
        # lose state.
        elif Combat.playerHP <= 0 and Combat.enemyHP > 0:
            print("""You fall at the hands of the mighty gladiator. Did you really stand a stand?!""")
            time.sleep(7)
            exit()
        elif Combat.playerHP <= 0 and Combat.enemyHP <= 0:
            # win state
            if Combat.playerHP > Combat.enemyHP:
                print("""The gladiator falls. Astonished, the crowd goes completely silent, then a great uproar fills the
colosseum once. A gladiator walks up to you with something in hand. "Please take this as a monument to your strength and
bravery." He hands you a celebratory dagger, with the writing "1. F" engraved on it. You try and ask him if he knows
anything about escaping the pentagon, but your question is utterly drowned out by the cheers of the crowd. You leave
the colosseum.
""")
                clues.append("1. F")
                Combat.gameWin = True
                break
            else:
            # lose state
                print("""You fall at the hands of the mighty gladiator. Did you really stand a stand?!""")
                time.sleep(7)
                exit()

# class and method for the final door.
class FinalRoom:
    password = "FEAR"
    answer = None
    attemptsMade = 3

def finalDoor():
    print("""Whether prepared or not, you make your way to the iron door. As you stand in front of it, you notice a LED
screen with the number three. There are four slots that each hold a character. A keyboard presents itself to you to
type out the password.
""")

    # enables the user to input a password as long as they have attempts remaining.

    while FinalRoom.attemptsMade > 0:
        if len(clues) == 0:
            print("You have no clues")
        elif len(clues) > 0:
            print("You clues are: {}".format(clues))
        print("What is the password?")
        FinalRoom.answer = input().upper()
        # win state.
        if FinalRoom.answer == FinalRoom.password:
            print("""All of a sudden, the power appears to go out in the room, shrouding you in complete darkness. Then
a rumbling noise can be heard in the distance, which is soon accompanied by a larger rumbling. The iron door starts to
shift, unveiling a tunnel, where a small light can be seen in the distance. You begin to sprint towards it, with the
light becoming larger as you close the distance, until you are greeted with the rushing winds of the great outdoors.
You have successfully escaped the pentagon!
""")
            time.sleep(10)
            exit()
        else:
            # subtracts an attempt upon an incorrect password.
            FinalRoom.attemptsMade = FinalRoom.attemptsMade - 1
            print("Incorrect password. You have {} attempts remaining.".format(FinalRoom.attemptsMade))

    if FinalRoom.attemptsMade <= 0:
        # lose state.
        print("""The LED screen drops from 1 to 0. Soon after, the floor begins to quake, opening a sinkhole, where you
truly will never escape from, as its epicentre sucks you into the depths of the pentagon.
""")
        time.sleep(7)
        exit()

nextStage = False
die = False

while nextStage == False:
    # game start.
    gameStart = None
    print("Welcome to Escape the Pentagon!")
    #  asks the user if they want to play.
    print("""You awake from a deep sleep and find yourself in a barren, pentagon shaped room. There is 
a door on each wall of the room, including a large steel door labelled 'E' with a four code lock. On this door, there
is a small note that reads: 'Forfeit your life, or challenge the Pentagon'. Do you accept the challenge? 
""")
    gameStart = input()
    try:
        if gameStart.lower() in ["y", "yes"]:
            print("""With not many other options, you yell at the top of your lungs that you accept this challenge.
Suddenly, you hear the sound of four locks unlocking. Aside from the large metal door, you realise
that the other doors are unlocked, labelled from A to E, with the large door being door E.
""")
            nextStage = True

        elif gameStart.lower() in ["n", "no"]:
            print("""With how incredibly silly this situation is, you simply tear up the note and begin looking for
alternate escape routes. Soon after, the ground begins to quake and a hole slowly begins to extend to the
edges of the room. With nowhere to run, you wait for your inevitable demise, as you finally sink into
the hole; the deep dark abyss, where your tale ends...
""")
            die = True
        else:
            raise ValueError("I can't have that as an answer!")
    except :
            nextStage = False

    # exits the program if the user says no.
    if die == True:
        time.sleep(7)
        exit()

while nextStage == True:
    # allows a user to select a room, which will take them to play the game.
    doorChoice = input("Which door will you check?")
    if doorChoice.lower() == "a":
        Pentajack()
    elif doorChoice.lower() == "b":
        codeCracker()
    elif doorChoice.lower() == "c":
        gameFramework()
    elif doorChoice.lower() == "d":
        mainUnscramble()
    elif doorChoice.lower() == "e":
        finalDoor()
    else:
        print("I can't have that as an answer.")