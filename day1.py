### Part 1 ###
with open("inputs/day1input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        calibration_value = int(digits[0] + digits[-1])
        total += calibration_value
print(total)

### Part 2 ###
import re
longhand_numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("inputs/day1input.txt", "r") as f:
    total2=0
    for line in f.readlines():
        found_digits = []
        for long_number in longhand_numbers:
            for m in re.finditer(long_number, line):
                found_digits.append([longhand_numbers[long_number], m.end()])
        found_digits.sort(key=lambda x: int(x[1]))
        calibration_value2 = found_digits[0][0]*10+found_digits[-1][0]
        total2 += calibration_value2

print(total2)