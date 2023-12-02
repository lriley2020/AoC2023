max_possible = {"red": 12, "green": 13, "blue": 14}

with open("inputs/day2input.txt", "r") as f:
    games = []
    for line in f.readlines():
        line = line.strip("\n")
        game_id = int(line.split(":")[0][4:])
        sets = line.split(":")[1].split("; ")
        for set in sets:
            toadd = []
            colours_with_occurences = set.split(",")
            for colour_with_occurence in colours_with_occurences:
                appearances, colour = colour_with_occurence.lstrip().split(" ")
                appearances = int(appearances)
                toadd.append((appearances, colour))
            sets[sets.index(set)] = toadd
        games.append([game_id, sets])

### Part 1 ###
sum_of_possible_ids = 0
for game in games:
    possible = True
    for thisset in game[1]:
        for this_colour_with_occurences in thisset:
            occurences_for_this_colour = this_colour_with_occurences[0]
            max_for_this_colour = max_possible[this_colour_with_occurences[1]]
            if occurences_for_this_colour > max_for_this_colour:
                possible = False
    if possible:
        sum_of_possible_ids += game[0]

print(f"Part 1, sum of possible game IDs: {sum_of_possible_ids}")


### Part 2 ###
sum_of_powers = 0
for game in games:
    max_for_each_colour = {"red": 0, "blue": 0, "green": 0}
    for thisset in game[1]:
        for this_colour_with_occurences in thisset:
            colour = this_colour_with_occurences[1]
            occurences_for_this_colour = this_colour_with_occurences[0]
            max_for_each_colour[colour] = occurences_for_this_colour if occurences_for_this_colour > max_for_each_colour[colour] else max_for_each_colour[colour]
    power = 1
    for max in max_for_each_colour.values():
        power *= max
    sum_of_powers+= power
print(f"Part 2, sum of powers on minimum combinations: {sum_of_powers}")