#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from player import Player
from hand import Hand

class Dealer(Player):

    def __init__(self):
        super().__init__()

    def deal(self, twocards):
        self.hands = [Hand(hidefirst=True)]
        self.activehandindex = 0
        self.activehand.add(twocards)
        self.printcards()

    def printcards(self):
        print("\nDealer hand:")
        self.activehand.showcards()
        if not self.activehand.hidefirstcard:
            print("Dealer total: " + str(self.activehand.score) + "\n")

    def reveal(self):
        self.activehand.hidefirstcard = False
        self.printcards()

    def dealerscore(self):
        return self.hands[0].score

    @property
    def activehand(self):
        return self.hands[0]






