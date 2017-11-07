#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydealer import Deck
from player import Player
from dealer import Dealer


class Table:
    shoe = None
    dealer = None
    player = None

    def __init__(self):
        self.shoe = Deck()
        self.shoe.rebuild = True
        self.shoe.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def playround(self):
        bet = int(self.player.getbet(10, 5000))
        self.dealer.deal(self.shoe.deal(2))
        self.player.deal(self.shoe.deal(2), bet)

        while not self.player.doneturn():
            playeraction = input("hit(h)/stay(s)/split(p)/doubledown(d)/insure(i)?:")
            if playeraction == "h":
                self.player.hit(self.shoe.deal(1))
            elif playeraction == "s":
                self.player.stay()
            elif playeraction == "p":
                if self.player.activehand.cansplit():
                    self.player.split(self.shoe.deal(2))
                else:
                    print("Can only split hand of two cards with the same value!")
            elif playeraction == "d":
                if self.player.activehand.candoubledown():
                    self.player.doubledown(self.shoe.deal(1))
                else:
                    print("Can only double down hand of two cards!")
            elif playeraction == "i":
                if self.dealer.activehand.isinsurable():
                    self.player.insure()
                else:
                    print("Can only insure when dealer has one facedown card and one ace!")

                    # elif playeraction == "u":
                    # Surrender?

        numberhands = str(len(self.player.hands))
        self.dealer.reveal()
        needgo = not self.player.allbust() and not self.player.allblackjack()

        if needgo:
            while self.dealer.activehand.score < 17:
                self.dealer.hit(self.shoe.deal(1))

            if self.dealer.allbust():
                # Dealer bust, each non-bust player hand yields its bet times 2
                for i, hand in enumerate(self.player.hands):
                    if not hand.isbust():
                        self.player.chips += hand.bet * 2
                        print("Hand " + str(i + 1) + " of " + numberhands + " wins " + str(hand.bet * 2))

        if self.dealer.allblackjack():
            print("Dealer blackjack!")
            if self.player.insured == True:
                self.player.chips += (bet * 1.5)
            for i, hand in enumerate(self.player.hands):
                if hand.isblackjack():
                    self.player.chips += hand.bet
                    print("Hand " + str(i + 1) + " of " + numberhands + " push...")
                    self.player.chips += bet
                else:
                    print("Hand " + str(i + 1) + " of " + numberhands + " loses!")

        else:
            for i, hand in enumerate(self.player.hands):
                if not hand.isbust() and not hand.isblackjack() and hand.score > self.dealer.dealerscore():
                    self.player.chips += hand.bet * 2
                    print("Hand " + str(i + 1) + " of " + numberhands + " wins " + str(hand.bet * 2))
                elif hand.isblackjack():
                    self.player.chips += hand.bet * 2.5
                    print("Hand " + str(i + 1) + " of " + numberhands + " blackjack! Wins " + str(hand.bet * 2.5))
                elif hand.isbust():
                    print("Hand " + str(i + 1) + " of " + numberhands + " loses!")
                elif hand.score < self.dealer.dealerscore() and not self.dealer.allbust():
                    print("Hand " + str(i + 1) + " of " + numberhands + " loses!")
                elif hand.score == self.dealer.dealerscore() and not self.dealer.allbust():
                    self.player.chips += hand.bet
                    print("Hand " + str(i + 1) + " of " + numberhands + " push...")