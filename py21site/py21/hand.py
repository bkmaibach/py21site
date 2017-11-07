#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pydealer

class Hand:
    _stack = None
    hidefirstcard = None
    _bust = None
    score = None
    bet = None

    def __init__(self, bet=0, hidefirst=False):
        self._stack = pydealer.Stack()
        self.hidefirstcard = hidefirst
        self.bet = bet

    def _cardvalue(self, card):
        return {
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'Jack': 10,
                'Queen': 10,
                'King': 10,
                'Ace':11
                }[card.value]

    def add(self, cards):
        self._stack += cards
        total = 0
        for card in self._stack:
            total += self._cardvalue(card)
        if total > 21:
            for card in self._stack:
                if card.value == "Ace":
                    total -= 10
                if total <= 21:
                    break
        if total > 21:
            self._bust = True
        else:
            self._bust = False
        self.score = total

    def getsize(self):
        return self._stack.size()

    def showcards(self):
        for i, card in enumerate(self._stack):
            if i == 0 and self.hidefirstcard == True:
                print('***FACEDOWN CARD***')
            else:
                print(card)

    def isbust(self):
        return self.score > 21

    def isblackjack(self):
        return self.score == 21 and self._stack.size == 2

    def isinsurable(self):
        return self._stack.size == 2 and self._stack[1].value == "Ace"

    def split(self):
        return self._stack.deal(1)

    def cansplit(self):
        return self._stack.size == 2 and self._cardvalue(self._stack[0]) == self._cardvalue(self._stack[1])

    def candoubledown(self):
        return self._stack.size == 2

    def doublebet(self):
        self.bet *= 2