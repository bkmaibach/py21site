#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from round import Table

table = Table()
play = True
while play == True:
    table.playround()
    yesno = input("Play again? (y/n):")
    if yesno == "y":
        play = True
    elif yesno == "n":
        play = False
