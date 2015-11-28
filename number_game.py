#!/usr/bin/env python
# Copyright 2015 Chris Heckler <hecklerchris@hotmail.com>
# GNU Affero General Public License version 3 (see the file LICENSE).

from random import randint

# Generates a number rom 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
while guesess_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You Win!"
        break
    guesses_left -= 1
else:
    print "You Lose."
