filename = "inputs\level2_input.txt"

encrypt_dict = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

score_choice = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
total = 0

with open(filename) as file:
    for line in file:
        score = 0
        choices = line.rstrip().split(" ")
        opponent = choices[0]
        choice = choices[1]

        score += score_choice[encrypt_dict[choice]]

        if encrypt_dict[opponent] == encrypt_dict[choice]:
            score += 3  # draw
        elif (
            (encrypt_dict[opponent] == "ROCK" and encrypt_dict[choice] == "PAPER")
            or (
                encrypt_dict[opponent] == "PAPER" and encrypt_dict[choice] == "SCISSORS"
            )
            or (encrypt_dict[opponent] == "SCISSORS" and encrypt_dict[choice] == "ROCK")
        ):
            score += 6  # win

        total += score


print(total)
