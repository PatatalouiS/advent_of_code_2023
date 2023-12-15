from utils import read_file
import math

COLORS = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

def count_is_possible(cube_count, cube_color):
    return cube_count <= COLORS[cube_color]

def set_is_possible(set):
    return all([count_is_possible(cube_count, cube_color) for cube_count, cube_color in set])
    
def game_is_possible(game):
    return all([set_is_possible(set) for set in game])

def compute_minimum_set(game):
	result = { color : 0 for color in COLORS.keys() }

	for set in game:
		for count, color in set:
			for compare_color in COLORS.keys():
				if (color == compare_color) and (result[compare_color] < count):
					result[compare_color] = count
	
	return result


def part_1(lines):
	result = 0
	parsed_games = []

	for game_index, line in enumerate(lines):
		_, game = line.split(':')
		game_sets = game.split(';')
		game_parsed = []

		for set in game_sets:
			cubes_strings = set.split(',')
			cubes_strings_parsed = []

			for cube in cubes_strings:
				cubes_count, cubes_color = cube.strip().split(' ')
				cubes_strings_parsed.append((int(cubes_count), cubes_color))

			game_parsed.append(cubes_strings_parsed)

		parsed_games.append(game_parsed)
    
		if game_is_possible(game_parsed):
			result += (game_index + 1)

	print(result)
	return result, parsed_games

def part_2(parsed_games):
	result = 0

	for game in parsed_games:
		minimum_set = compute_minimum_set(game)
		power = math.prod(minimum_set.values())
		result += power

	print(result)
	return result


def main():
    lines = read_file('./day_2/file.txt')
    _, parsed_games = part_1(lines)
    part_2(parsed_games)