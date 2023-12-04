### Part 1 ###

total = 0
with open("inputs/day4input.txt", "r") as f:
    for line in f.readlines():
        line = line.split(":", 1)[1].strip("\n")
        our_numbers, winning_numbers = line.split("|")
        our_numbers = our_numbers.split(" ")
        winning_numbers = winning_numbers.split(" ")
        our_numbers = list(filter(None, our_numbers))
        winning_numbers = list(filter(None, winning_numbers))
        matches = len([x for x in our_numbers if x in winning_numbers])
        score = 1 * 2 ** (matches - 1) if matches != 0 else matches
        total += score

print(total)


### Warning - this code is incredibly inefficient - it took around 1 and a half minutes to get the solution, please do not look! ###
### Part 2 ###

cards_and_matches = []

with open("inputs/day4input.txt", "r") as f:
    for line in f.readlines():
        cardnumberpart = line.split(":", 1)[0]
        cardnumber = [int(i) for i in cardnumberpart.split() if i.isdigit()][0]
        line = line.split(":", 1)[1].strip("\n")
        our_numbers, winning_numbers = line.split("|")
        our_numbers = our_numbers.split(" ")
        winning_numbers = winning_numbers.split(" ")
        our_numbers = list(filter(None, our_numbers))
        winning_numbers = list(filter(None, winning_numbers))
        matches = len([x for x in our_numbers if x in winning_numbers])
        cards_and_matches.append([cardnumber, matches])

for current_card_number in range(1, len(cards_and_matches) + 1):

    matching_cards = []
    for card in cards_and_matches:
        if card[0] == current_card_number:
            matching_cards.append(card)
    number_of_cards_with_the_current_card_number = len(matching_cards)
    score_for_currrent_card_number = matching_cards[0][1]
    for card_number_to_add in range(current_card_number + 1, current_card_number + score_for_currrent_card_number + 1):
        ## Find the matches of the card number that we are adding ##
        for cardtofindvaluefor in cards_and_matches:
            if cardtofindvaluefor[0] == card_number_to_add:
                matchesforcardtoadd = cardtofindvaluefor[1]
        ## Add an element with the value [card_number_to_add, matches of card we're adding] n times where n is the number matches for this card
        for i in range(number_of_cards_with_the_current_card_number):
            cards_and_matches.append([card_number_to_add, matchesforcardtoadd])

print(len(cards_and_matches))
