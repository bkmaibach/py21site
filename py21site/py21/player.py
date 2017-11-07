#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hand import Hand


class Player:
    _hands = []
    chips = None
    insured = None
    _activehandindex = None
    _initialbet = None

    def __init__(self):
        self.chips = 5000
        self._initialbet = 100

    def deal(self, twocards, initialbet):
        self.hands = [Hand(bet=initialbet, hidefirst=False)]
        self._initialbet = initialbet
        self.insured = False
        self.activehandindex = 0
        self.activehand.add(twocards)
        self.printcards()

    def hit(self, card):
        self.activehand.add(card)
        self.printcards()
        if self.activehand.isbust():
            print("Bust!")
            self.nexthand()

    def stay(self):
        self.nexthand()

    def doubledown(self, card):
        self.chips -= self._initialbet
        self.activehand.doublebet()
        self.activehand.add(card)
        self.printcards()
        if self.activehand.isbust():
            print("Bust!")
        self.nexthand()

    def split(self, twocards):
        self.chips -= self._initialbet
        self.hands.insert(self.activehandindex + 1, Hand(bet=self.activehand.bet))
        self.hands[self.activehandindex + 1].add(self.activehand.split())
        self.activehand.add(twocards.split()[0])
        self.hands[self.activehandindex + 1].add(twocards.split()[1])
        self.printcards()

    def insure(self):
        self.chips -= self._initialbet/2
        self.insured = True

    def printcards(self):
        for i, hand in enumerate(self.hands):
            print("\nPlayer hand " + str(i + 1) + " of " + str(len(self.hands)) + ":")
            hand.showcards()
            print("Hand total: " + str(hand.score) + "\n")

    @property
    def activehand(self):
        return self.hands[self.activehandindex]

    # @property.setter
    # def activehand(self):

    def nexthand(self):
        self.activehandindex += 1

    def doneturn(self):
        return self.activehandindex >= len(self.hands)

    def getbet(self, min, max):
        print("Chips available: " + str(self.chips))
        bet = 0
        while bet < min or bet > max or bet > self.chips:
            print("Place your bet, or press enter to reuse " + str(self._initialbet))
            playerinput = input("(minimum " + str(min) + ", maximum " + str(max) + "):")
            if playerinput == "":
                bet = self._initialbet
            else:
                bet = int(playerinput)
        self.chips -= bet
        return bet

    # The dealer doesn't need to go if all the players hands are bust.
    # This is essential to the dealers advantage over the player.
    def allbust(self):
        for hand in self.hands:
            if not hand.isbust():
                return False
        return True

    def allblackjack(self):
        for hand in self.hands:
            if not hand.isblackjack():
                return False
        return True