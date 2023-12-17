from utils import read_file
import numpy as np


def find_motor_numbers(motor_schema):
  numbers = []
  current_string_number = ""
  current_start_position = None
  current_end_position = None

  for line_index, line_array in enumerate(motor_schema):
    for char_index, char in enumerate(line_array):
      if char.isdigit():
        if current_string_number == '':
          current_start_position = [line_index, char_index]
        current_string_number += char
      elif current_string_number != '':
        current_end_position = [line_index, char_index - 1]
        numbers.append({ 
          "number" : current_string_number,
          "start_position" : current_start_position,
          "end_position" : current_end_position
        })
        current_string_number = ""

  return numbers

def get_part_adjacent_positions(motor_number):
  [start_line,  start_column] = motor_number["start_position"]
  [end_line, end_column] = motor_number["end_position"]

  return [
    (start_line, start_column - 1),
    (start_line, end_column + 1),
    *[(start_line - 1, column) for column in range(start_column - 1, end_column + 2)],
    *[(start_line + 1, column) for column in range(start_column - 1, end_column + 2)],
  ]


def is_a_magic_number(motor_number, motor_schema):
  for line, column in get_part_adjacent_positions(motor_number):
    value = motor_schema[line, column]
    if (not value.isdigit()) and (value != "."):
      return True

  return False


def find_stars(motor_schema):
  stars = []
  for line_index, line_array in enumerate(motor_schema):
    for char_index, char in enumerate(line_array):
      if char == "*":
        stars.append((line_index, char_index))
  return stars


def find_gears(stars, part_numbers):
  gears = []

  for star in stars:
    adjacent_part_numbers = [
      part_number for part_number in part_numbers if star in get_part_adjacent_positions(part_number)
    ]
    
    if len(adjacent_part_numbers) == 2:
      gears.append((star, adjacent_part_numbers))

  return gears


def part_1(lines):
  # Add padding
  motor_shape = (len(lines) + 2, len(lines[0].strip()) + 2)
  motor_schema_parsed = np.full(motor_shape, ".", dtype=str)

  # Parse motor schema
  for line_index, line in enumerate(lines):
    line_array = [".", *list(line.strip()), "."]
    motor_schema_parsed[line_index + 1, :] = line_array

  motor_numbers = find_motor_numbers(motor_schema_parsed)
  magic_numbers = [
    motor_number for motor_number in motor_numbers if is_a_magic_number(motor_number, motor_schema_parsed)
  ]

  result = sum([int(motor_number["number"]) for motor_number in magic_numbers])

  print(result)
  return result, magic_numbers, motor_schema_parsed

def part_2(part_numbers, motor_schema):
  stars = find_stars(motor_schema)
  gears = find_gears(stars, part_numbers)
  result = 0

  for _, [number_1, number_2] in gears:
    result += int(number_1["number"]) * int(number_2["number"])
    
  print(result)
  return result
  

def main():
  lines = read_file('./day_3/file.txt')
  _, part_numbers, motor_schema = part_1(lines)
  part_2(part_numbers, motor_schema)