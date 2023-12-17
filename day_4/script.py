from utils import read_file
import re


def remove_trailing_and_multiple_spaces(line):
  return re.sub(' +', ' ', line.strip())


def part_1(lines):
  cards_parsed = []
  
  for line in lines:
    _, numbers = line.split(':')
    winning_numbers_string, all_numbers_string = numbers.split('|')
    winning_numbers = remove_trailing_and_multiple_spaces(winning_numbers_string).split(' ')
    all_numbers = remove_trailing_and_multiple_spaces(all_numbers_string).split(' ')
    cards_parsed.append((winning_numbers, all_numbers)) 

  points = 0

  for winning_numbers, all_numbers in cards_parsed:
    intersection = list(set(winning_numbers).intersection(set(all_numbers)))
    nb_good_numbers = len(intersection)

    if nb_good_numbers:
      points += 2 ** (nb_good_numbers - 1)

  print(points)
  return points, cards_parsed
  

def part_2(cards):
  nb_of_each_cards = [1 for _ in range(len(cards))]

  for card_number, (winning_numbers, all_numbers) in enumerate(cards):
    intersection = list(set(winning_numbers).intersection(set(all_numbers)))
    nb_good_numbers = len(intersection)

    if nb_good_numbers:
      cards_won = list(range(card_number + 1, nb_good_numbers + card_number + 1))
      for card_won in cards_won:
        nb_of_each_cards[card_won] += nb_of_each_cards[card_number]

  result = sum(nb_of_each_cards)
  print(result)
  return result

def main():
  lines = read_file('./day_4/file.txt')
  _, cards_parsed = part_1(lines)
  part_2(cards_parsed)