from deck import Deck
from player import Player
import os


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')


def print_logo():
    print("""  _                     _           _            _
 | |    ___  _ __   ___| |_   _    | | __ _  ___| | __
 | |   / _ \\| '_ \\ / _ \\ | | | |_  | |/ _` |/ __| |/ /
 | |__| (_) | | | |  __/ | |_| | |_| | (_| | (__|   <
 |_____\\___/|_| |_|\\___|_|\\__, |\\___/ \\__,_|\\___|_|\\_\\
 ------------------------ |___/ ----------------------
    """)


def create_deck():
    deck = Deck()
    deck.random()
    return deck


def draw_cards(deck, number):
    if number < 1:
        raise ValueError("number must be higher than 0")
    return deck.cards.pop() if number == 1 else [deck.cards.pop() for _ in range(number)]


def print_house(house, hidden=True):
    printArr = []
    for card in house.hand:
        printArr.append(str(card))
    if hidden:
        printArr[0] = "XX"
    print("House: " + ' '.join(printArr))
    if not hidden:
        print('- score: ' + str(house.score))


def print_result(house, player):
    print("--------------\n")
    print_house(house, False)
    print('\nPlayer: ' + str(player))


def print_info(house, player):
    clear_screen()
    print_logo()
    print_house(house)
    print('\nPlayer: ' + str(player))


def print_options():
    print("\n-- Options --")
    print(" 1 : bet money")
    print(" 2 : draw card")
    print(" 3 : buy in")
    print(" 4 : pass")
#    print(" 5 : split cards")
    print("\nWhat do you want to do?", end=' ')


def players_turn(deck, player, option=0):
    if option == 0:
        print_options()
        option = input()
        if not option.isnumeric():
            return players_turn(deck, player)
        option = int(option)
        if option not in range(1, 5):
            return players_turn(deck, player)

    if option == 1:
        amount = input("How much money do you want to bet? ")
        if not amount.isnumeric:
            return players_turn(deck, player, option)
        try:
            player.bet(int(amount))
            print_info(house, player)
        except ValueError as e:
            print(e)
            return players_turn(deck, player, option)
        return players_turn(deck, player)

    elif option == 2:
        player.hit(draw_cards(cardDeck, 1))
        print_info(house, player)
        return True

    elif option == 3:
        amount = input("With how much money do you want to buy in? ")
        if not amount.isnumeric:
            return players_turn(deck, player, option)
        try:
            player.buy_in(int(amount))
            print_info(house, player)
        except ValueError as e:
            print(e)
            return players_turn(deck, player, option)
        return players_turn(deck, player)

    elif option == 4:
        return False


def house_playing(deck, house):
    while(house.score < 16):
        house.hit(draw_cards(cardDeck, 1))


def check_blackjack(house, player):
    if player.has_blackjack():
        if house.has_blackjack():
            player.draw()
        else:
            player.win()


def check_winner(house, player):
    check_blackjack(house, player)
    if player.score > 21:
        if house.score > 21:
            player.draw()
        else:
            player.lose()
    elif player.score > house.score:
        player.win()
    elif player.score == house.score:
        player.draw()
    else:
        if house.score > 21:
            player.win()
        else:
            player.lose()

# Start Game


player = Player()
house = Player()

while True:
    cardDeck = create_deck()

    player.play(draw_cards(cardDeck, 2))
    house.play(draw_cards(cardDeck, 2))

    print_info(house, player)

    check_blackjack(house, player)
    players_turn(cardDeck, player)
    card_drawn = False
    while(card_drawn and player.score < 21):
        card_drawn = players_turn(cardDeck, player)
    house_playing(cardDeck, house)
    check_winner(house, player)
    print_result(house, player)
    again = input("\nDo you want to play another round? (y/n) ")
    if again != "y":
        print("All your money will be lost!")
        again = input(
            "Do you really want to quit? (y/n) ")
        if again == "y":
            break
