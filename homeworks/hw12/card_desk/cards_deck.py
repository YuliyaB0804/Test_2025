# Колода карт
# Напишите программу которая содержит список карт, умеет их перемешивать и
# позволяет пользователю достать карту из колоды по ее номеру. Всего в колоде
# 54 карт. Класс Card содержит спискок номеров карт и список мастей.
#
# class Card:
#     number_list = ...
#     mast_list = ...
#
#     def __init__(self):
#         ...
#
# class CardsDeck:
#     def __init__(self):
#         ...
#
#
# deck = CardsDeck()
# deck.shuffle()
# card_number = int(input('Выберите карту из колоды в 54 карт:'))
# card = deck.get(card_number)
# print(f'You card is: {card}')
# >> Hearts 10
#
# card_number = int(input('Выберите карту из колоды в 54 карт:'))
# card = deck.get(card_number)
# print(f'You card is: {card}')
# >> Diamonds 6

import random


class Card:
    number_list = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.mast} {self.number}"


class CardsDeck:
    def __init__(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        self.cards.append(Card('Joker', 'None'))
        self.cards.append(Card('Joker', 'None'))
        self.remaining_cards = self.cards.copy()

    def shuffle(self):
        random.shuffle(self.remaining_cards)

    def get_card(self, number):
        if not isinstance(number, int):
            raise ValueError("Error: enter a card number from 1 to 54")
        if not 1 <= number <= len(self.remaining_cards):
            raise ValueError("Error: enter a card number from 1 to 54")
        current_card = self.remaining_cards.pop(number - 1)
        return current_card

    def get_remaining_cards(self):
        return self.remaining_cards

    def _card_validator(self, number):
        if isinstance(number, int) and 1 <= number <= len(self.cards):
            return number
        else:
            raise ValueError("Error: enter a card number from 1 to 54")


deck = CardsDeck()
deck.shuffle()


try:
    card_number = int(input('Выберите карту из колоды в 54 карты: '))
    card = deck.get_card(card_number)
    print(f'Your card is: {card}')
except ValueError as e:
    print(e)

try:
    card_number = int(input('Выберите другую карту из колоды в 54 карты: '))
    card = deck.get_card(card_number)
    print(f'Your card is: {card}')
except ValueError as e:
    print(e)
