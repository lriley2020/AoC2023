import re
from math import sqrt, ceil

def quadratic_solver(a, b, c):
    discriminant = (b**2) - (4*a*c)
    solution1 = (-b+sqrt(discriminant))/(2*a)
    solution2 = (-b-sqrt(discriminant))/(2*a)
    return [ceil(solution1), int(solution2)]

## Part 1 ##
with open("inputs/day6input.txt", "r") as f:
    contents = f.readlines()
    times = re.findall(r'\d+', contents[0])
    times = [int(x) for x in times]
    distances = re.findall(r'\d+', contents[1])
    distances = [int(x) for x in distances]
    races = list(zip(times, distances))

error_margin = 1
for race in races:
    race_time, race_distace = race
    boundaries = quadratic_solver(1, -race_time, race_distace)
    number_of_possible_times = max(boundaries) - min(boundaries) - 1
    error_margin *= number_of_possible_times

print(error_margin)


### Part 2 ###
race_time_parts, race_distace_parts = zip(*races)
real_race_time = int(''.join([str(x) for x in race_time_parts]))
real_race_distace = int(''.join([str(x) for x in race_distace_parts]))
real_boundaries = quadratic_solver(1, -real_race_time, real_race_distace)
real_number_of_possible_times = max(real_boundaries) - min(real_boundaries) - 1
print(real_number_of_possible_times)
