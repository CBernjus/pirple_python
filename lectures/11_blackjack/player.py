from deck import Deck


class Player:

    def __init__(self, hand=[], money=100.0):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.current_bet = 0.0

    def __str__(self):
        return ' '.join([str(card) for card in self.hand]) + '\n- score: ' + str(self.score) + '\n- money: ' + str(self.money) + '\n- bet: ' + str(self.current_bet)

    def set_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            score += card.value
            if card.face == "A":
                aces += 1
                if score > 21:
                    score -= 10
                    aces -= 1
        return score

    def has_blackjack(self):
        return self.score == 21 and len(self.hand) == 2

    def hit(self, card):
        if card in self.hand:
            raise ValueError("card already in hand")
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def buy_in(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        self.money += amount

    def bet(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if amount > self.money:
            raise ValueError("not enough money")
        self.money -= amount
        self.current_bet += amount

    def draw(self):
        print("\nIt's a draw! You get " + str(self.current_bet) + " back")
        self.money += self.current_bet
        self.current_bet = 0.0

    def win(self):
        profit = 0
        if self.has_blackjack():
            profit = 2.5 * self.current_bet
        else:
            profit = 2 * self.current_bet
        self.money = profit
        print("\nYou win " + str(profit))
        self.current_bet = 0.0

    def lose(self):
        print("\nYou lost " + str(self.current_bet))
        self.current_bet = 0.0
