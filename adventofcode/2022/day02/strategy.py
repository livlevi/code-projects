# Open file, read first character, ignore blank, read next character
# Logic for rock paper scissors, record it as a win. 
# Rock wins vs scissors, loses against paper
# scissors wins vs paper, loses against rock
# paper wins vs rock, loses against scissors
# add points

file_name = "plays.txt"
play = ""
total_score = 0

# ROCK = A or X
# PAPER = B or Y
# SCISSORS = C or Z

with open (file_name, "r") as file:

    #line = file.readline()
    #.strip()

    for line in file:
        
        play = line[0] + line[2]
        if play == "AX":
            total_score += 4
        elif play == "BX":
            total_score += 1
        elif play == "CX":
            total_score += 7
        elif play == "AY":
            total_score += 8
        elif play == "BY":
            total_score += 5
        elif play == "CY":
            total_score += 2
        elif play == "AZ":
            total_score += 3
        elif play == "BZ":
            total_score += 9
        elif play == "CZ":
            total_score += 6
        print(play)
     
print("## Total Score: ##")
print(total_score)