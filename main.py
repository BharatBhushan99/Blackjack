import random 

import graphics

# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def adjust_ace(cards):

  while sum(cards) > 21 and 11 in cards:
    ace_index = cards.index(11)
    cards[ace_index] = 1

def print_scores(player_cards, computer_cards):
  print(f"\tYour final hand: {player_cards}, final score: {sum(player_cards)}")
  print(f"\tComputer’s final hand: {computer_cards}, final score: {sum(computer_cards)}")

def start_game():

  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  # clear()

  player_cards = []
  computer_cards = []


  if play_game == 'y':

    print(graphics.logo)
    should_continue = True

    player_cards = [random.choice(cards), random.choice(cards)]

    computer_cards = [random.choice(cards), random.choice(cards)]

    while should_continue:

      adjust_ace(player_cards)

      print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
      print(f"\tComputer’s first card: {computer_cards[0]}")

      if sum(player_cards) > 21:
        print_scores(player_cards, computer_cards)
        print("You went over. You lose 😭")
        should_continue = False
      else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit == 'y':
          player_cards.append(random.choice(cards))
        else:
          should_continue = False

    if sum(player_cards) <= 21:

      while sum(computer_cards) <= sum(player_cards):
        computer_cards.append(random.choice(cards))
        adjust_ace(computer_cards)

      if sum(computer_cards) > 21:
        print_scores(player_cards, computer_cards)
        print("Opponent went over. You win 😁")
      elif sum(computer_cards) == sum(player_cards):
        print_scores(player_cards, computer_cards)
        print("Draw 🙃")
      else:
        print_scores(player_cards, computer_cards)
        print("You lose 😤")

    start_game()    

start_game()


