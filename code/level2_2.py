filename = "inputs\level2_input.txt"

encrypt_dict = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

score_choice = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
total = 0

with open(filename) as file:
    for line in file:
        score = 0
        choices = line.rstrip().split(" ")
        end_state = choices[1]
        opponent = choices[0]

        if encrypt_dict[end_state] == "DRAW":
            score += score_choice[encrypt_dict[opponent]]
            score += 3
        elif encrypt_dict[end_state] == "WIN":
            score += 6
            if encrypt_dict[opponent] == "ROCK":
                score += score_choice[encrypt_dict["B"]]
            elif encrypt_dict[opponent] == "PAPER":
                score += score_choice[encrypt_dict["C"]]
            elif encrypt_dict[opponent] == "SCISSORS":
                score += score_choice[encrypt_dict["A"]]
        else:
            if encrypt_dict[opponent] == "ROCK":
                score += score_choice[encrypt_dict["C"]]
            elif encrypt_dict[opponent] == "PAPER":
                score += score_choice[encrypt_dict["A"]]
            elif encrypt_dict[opponent] == "SCISSORS":
                score += score_choice[encrypt_dict["B"]]

        total += score


print(total)
