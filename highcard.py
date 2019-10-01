#!/usr/bin/python
###Written by Larry Walters larwal.dev###
###High card game###

from time import sleep
from random import randint, seed

seed_value = randint(1,99)
seed(seed_value)

def computers_card():
    comp_card = randint(1,13)
    return comp_card

def players_card():
    player_card = randint(1,13)
    return player_card

def rename_face_cards(card):
    if card == 1:
        card_value = "Ace"
    elif card == 11:
        card_value = "Jack"
    elif card == 12:
        card_value = "Queen"
    elif card == 13:
        card_value = "King"
    else:
        card_value = card
    return card_value

def compare_cards(comp_card, comp_card_value, player_card, player_card_value):
    print("The player drew a(n): %s" %(player_card_value))
    print("The computer drew a(n): %s" %(comp_card_value)) 
    sleep(1)

    if player_card == comp_card:
        print("It was a tie.\nThe win defaults to the player!")
    elif player_card > comp_card:
        print("You won!")
    elif player_card < comp_card:
        print("The computer won.\nBetter luck next time.")

if __name__ == '__main__':
    print("Lets play high card.")
    print("To win you have to draw a higher card then the computer.")
    print("Aces are low cards.")
    sleep(3)
    print("Drawing the player's card...")
    player_card = players_card()
    sleep(1.5)
    print("Drawing the computer's card...")
    comp_card = computers_card()
    sleep(1.5)
    player_card_value = rename_face_cards(player_card)
    comp_card_value = rename_face_cards(comp_card)
    compare_cards(comp_card, comp_card_value, player_card, player_card_value)
