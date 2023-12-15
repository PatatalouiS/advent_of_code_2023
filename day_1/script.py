from utils import read_file

DIGITS_MAPPER = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def part_1(lines):    
  result = 0

  for line in lines:
      digit_array = [
          int(char) for char in line if char.isdigit()
      ]
      
      result += int(str(digit_array[0]) + str(digit_array[-1]))

  print(result)
  return result


def part_2(lines):
    result = 0

    for line in lines:
        digits_in_line = []
        for offset in range(len(line)):
            current_char = line[offset]
            if current_char.isdigit():
                digits_in_line.append(int(current_char))

            for string_digit in DIGITS_MAPPER.keys():
                end_offset = offset + len(string_digit)
                if end_offset < len(line):
                    if line[offset:end_offset] == string_digit:
                        digits_in_line.append(DIGITS_MAPPER[string_digit])
                        break
        
        if len(digits_in_line):
          result += int(str(digits_in_line[0]) + str(digits_in_line[-1]))

    print(result)
    return result
   

def main():
    lines = read_file('./day_1/file.txt')
    part_1(lines)
    part_2(lines)
    
