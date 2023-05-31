# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import OrderedDict
import random
import sys
import time
turn = 0
asked1 = []
players = []
names = []
deck = []

def secondturnstart(asked1, players, names, deck, turn, newturn, pesca):
    print(f"isto e {turn}")
    asked = input(
        f"hi {names[0]} so this is your cards {players[names[0]]} \nplease write the name of a player you want to ask a card for: first name and then the card")
    asked1 = asked.split()
    print(players)
    print(asked1)
    if asked1[1].isdigit():
        carta = int(asked1[1])
        if carta in players[names[0]]:
            print("You have that card")
            print(f"Good job \n you can play again !")
            play(asked1, players, names, deck, turn, newturn, secondturnstart)
        else:
            print("You dont have that card \n try again please ")
            turnstart(asked1, players, names, deck, turn, newturn, secondturnstart)
    elif isinstance(asked1[1], str):
        carta = asked1[1]
        if carta in players[names[0]]:
            print("You have that card")
            print(f"Good job \n you can play again !")
            play(asked1, players, names, deck, turn, newturn, secondturnstart)
        else:
            print("maybe you didn't write it right try again")
    pesca(asked1, players, names, deck, turn, newturn, secondturnstart)



def newturn(asked1, players, names, deck, turn, secondturnstart):
    idk = []
    idk.append(asked1[0])
    asked = input(
        f"hi {idk[0]} so this is your cards {players[idk[0]]} \nplease write the name of a player you want to ask a card for: first name and then the card")
    asked1 = asked.split()
    print(players)
    print(asked1)
    if asked1[1].isdigit():
        carta = int(asked1[1])
        if carta in players[idk[0]]:
            print("You have that card")
            print(f"Good job \n you can play again !")
            secondturnstart(asked1, players, names, deck, turn, newturn )
        else:
            print("You dont have that card \n try again please ")
            secondturnstart(asked1, players, names, deck, turn, newturn ,)
    elif isinstance(asked1[1], str):
        carta = asked1[1]
        if carta in players[idk[0]]:
            print("You have that card")
            secondturnstart(asked1, players, names, deck, turn, newturn ,)
            print(f"Good job \n you can play again !")
        else:
            print("maybe you didn't write it right try again")
            secondturnstart(asked1, players, names, deck, turn, newturn, )
    idk.remove(asked1[0])
    pesca(asked1, players, names, deck, turn)


def play(asked1, players, names, deck, turn , newturn , secondturnstart, pesca):
    if asked1[1].isdigit():
        carta = int(asked1[1])
        if carta in players[asked1[0]]:
            nrcart = players[asked1[0]].count(carta)
            print(f"Alright {asked1[0]} had {nrcart} {asked1[1]}")
            if asked1[0] in players and isinstance(players[asked1[0]], list):
                players[asked1[0]] = [val for val in players[asked1[0]] if val != int(asked1[1])]
            for s in range(nrcart):
                if carta == "10":
                    players[names[0]].extend(asked1[1] * 2)
                else:
                    players[names[0]].extend(asked1[1])
            print(players)
            secondturnstart(asked1, players, names, deck, turn , newturn , pesca)

        else:

            pesca(asked1, players, names, deck, turn, secondturnstart , newturn)


    elif isinstance(asked1[1], str):
        carta = asked1[1]
        if carta in players[asked1[0]]:
            nrcart = str(players[asked1[0]].count(asked1[1]))
            nrcart2 = int(nrcart)
            print(f"Alright {asked1[0]} has {nrcart} {asked1[1]}  aa")
            print("right22")
            if asked1[0] in players and isinstance(players[asked1[0]], list):
                players[asked1[0]] = [val for val in players[asked1[0]] if val != str(asked1[1])]
            for s in range(nrcart2):
                players[names[0]].append(asked1[1])
            print(players)
            secondturnstart(asked1, players, names, deck, turn)

        else:
            pesca(asked1, players, names, deck)




def pesca(asked1, players, names, deck, turn, secondturnstart , newturn ):

    print(f"Sorry {asked1[0]} doesnt have any {asked1[1]} ")
    print("go fishing!")
    print("waiting for a bite ..")
    sorte = random.choice(deck)
    players[names[0]].append(sorte)
    deck.remove(sorte)
    print(f"you got {sorte}")
    print(f"this is your cards now {players[names[0]]}")
    newturn(asked1, players, names, deck, turn , secondturnstart)

    return turn

def functionstart(turn,):
    print("""
    Hello,Welcome to my first program in python
    You can choose between three games!
    The first one is a simple guess the number called Guesser
    The second one is a card game called fishing
    The third one is still in development
    """)
    nome = input("Whats your name?")
    game = input(f"""alright, Welcome {nome}, 
    so what game would you like to play ?
    """)
    if game == "Guesser":
        functionguessinggame(nome,)
    elif game == "fishing":
        functionfishinggame(nome, turn, newturn, asked1, players, names, deck=deck, secondturnstart=secondturnstart)

    else:
        print(f"sorry something went wrong try again")
    return nome


def functionguessinggame(nome):
    # guessing game
    print("""
    So there's three level of difficulty
    beginners level has a range between 1 and 25
    Casual level has a range between 1 and 100 
    Im crazy level has a range between 1 and 1000""")
    playerslevel = input("""
        So what level would you like to play? 
        Write beginners for beginners
        Write casual for casual
        Write crazy for crazy?""")
    if playerslevel == "beginners":
        trys1 = 5
        print("Hi " + nome)
        print(f"""
        Lets start our game you will get {trys1} chances to guess the number you will get some tips 
        like if are close to the number you will be hot "
        if you are cold it means the guess its still pretty far away """)
        secret = random.randint(1, 25)

    elif playerslevel == "casual":
        trys1 = 10
        print("Hi " + nome)
        print(f"""
        Lets start our game you will get {trys1} chances to guess the number you will get some tips 
        like if are close to the number you will be hot "
        if you are cold it means the guess its still pretty far away""")
        secret = random.randint(1, 50)

    elif playerslevel == "crazy":
        trys1 = 25
        print("Hi " + nome)
        print(f"""
        Lets start our game you will get {trys1} chances to guess the number you will get some tips 
        if you are close to the number you will be hot "
        if you are cold it means the guess its still pretty far away """)
        secret = random.randint(1, 1000)

    else:
        print("Sorry something went wrong you really need to type the difficult level as beginners,casual or crazy")
    print("""Okay!
    lets start the game!""")
    endgame = False
    guess = int(input(" okay so tell me whats your first guess!"))
    if guess != secret:
        while endgame == False:
            trys = trys1 - 1
            diff = guess - secret
            realdiff = abs(diff)
            around1 = realdiff / 2
            around = round(around1)
            if guess > secret:
                print(f"ahhh you are feeling kinda cold you get {trys} more trys good luck player !")
                print(f"theres a difference around {around}")
                guess = int(input(" whats your next guess!"))
            elif guess < secret:
                print(f"ahhh you are feeling kinda cold you get {trys} more trys good luck player !")
                print(f"theres a difference around {around}")
                guess = int(input(" whats your next guess!"))
            else:
                endgame = True
                print(f"good job your guess was right the number was indeed {guess}")
                print("the game is going to end")
                restart = input("would you like to restart ? yes or no ?")
                if restart == "yes":
                    functionstart()
                else:
                    print("alright, the program is going to close! see you next time")
                    sys.exit()
    else:
        print("Ah shit man you got it on first guess")
        functionstart(turn,)


def functionfishinggame(nome, turn, newturn, asked1, players, names, secondturnstart, deck):
    print(f"""
    Hi {nome} so im gonna explain the rules of this game.
    First this game used a deck of 52 cards all the cards expect the jokers.
    Every player will start with 4 cards.
    The objective of the game is collecting all the 4 of each card (4 Aces, 4 Kings, 4 Queens, etc.)
    Its by turns
    When its a players turn they will have one chance of asking one card from their hand to another player
    If the player has any of the card that was asked they must give all the cards they hold to the player adn that player will have another chance to ask for another card 
    If the player that was asked for a card doesnt have any, the player asking for the card must go fishing into the deck for one card , if by luck its the same card as he ask he can ask again for another card but he has to prove that the card that he fished is the same as he asked.
    the game ends when theres no more cards to ask for.
    The player that gets asked the card and doesnt have it will be the one asking next
    When you get 4 of the same cards you will place them out of the way and that will count as one fish.
    the player with most fishes wins.
    GOOD LUCK !  
    """)
    deck = list([num for num in range(1, 14) for _ in range(4)])

    sub = {1: "Valete", 11: "AS", 12: "Dama", 13: "Rei"}
    for i in range(len(deck)):
        if deck[i] in sub:
            deck[i] = sub[deck[i]]
    nrplayer = None
    a = 0
    while a != nrplayer:
        nrplayer = int(input("So how many of real players are going to play?between 1 and 4"))
        players = {}
        playerss = input("So please write every players name with spaces please")
        playerstye = playerss.split()
        a = len(playerstye)
        if a != nrplayer:
            print("Sorry the number of players doesnt match the number of names that you gave, start over")

    for name in playerstye:
        players[name] = []
    for _ in range(4):
        for name in players.keys():
            sorte = random.choice(deck)
            players[name].append(sorte)
            deck.remove(sorte)
    print(players)
    names = list(players.keys())
    if names[0] in players.keys():
        asked = input(
            f"hi {names[0]} so this is your cards {players[names[0]]} \nplease write the name of a player you want to ask a card for: first name and then the card")
        asked1 = asked.split()
        print(players)
        print(asked1)
        if asked1[1].isdigit():
            carta = int(asked1[1])
            if carta in players[names[0]]:
                print("You have that card")
                play(asked1, players, names, deck, turn, newturn , secondturnstart , pesca )
            else:
                print("You dont have that card \n try again please")
        elif isinstance(asked1[1], str):
            carta = asked1[1]
            if carta in players[names[0]]:
                print("You have that card")
                play(asked1, players, names, deck, turn, newturn , secondturnstart , pesca)
            else:
                print("maybe you didn't write it right")
    while len(deck) != 0:
        if asked1[0] in players.keys():
            newturn(asked1, players, names, deck,turn)

functionstart(turn, )


