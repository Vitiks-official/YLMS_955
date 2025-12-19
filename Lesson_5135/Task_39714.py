nums = int(input())
scoreAI, scorePL = 0, 0
letters = ["_"] * nums
whos_step = False
while letters.count("_"):
    if whos_step:
        place, color = input().split()
        while letters[int(place)] != "_":
            print("This place is taken.")
            place, color = input().split()
        print(f"Your step {place} {color}")
        letters[int(place)] = color
        print(" ".join(letters))
    else:
        print(f"AI step {letters.index("_")} R")
        letters[letters.index("_")] = "R"
        print(" ".join(letters))
    if "".join(letters).count("RRR"):
        k = "".join(letters).find("RRR")
        letters[k], letters[k + 1], letters[k + 2] = "_", "_", "_"
        print(" ".join(letters))
        if whos_step:
            scorePL += 1
        else:
            scoreAI += 1
    if "".join(letters).count("BBB"):
        k = "".join(letters).find("BBB")
        letters[k], letters[k + 1], letters[k + 2] = "_", "_", "_"
        print(" ".join(letters))
        if whos_step:
            scorePL += 1
        else:
            scoreAI += 1
    if "".join(letters).count("GGG"):
        k = "".join(letters).find("GGG")
        letters[k], letters[k + 1], letters[k + 2] = "_", "_", "_"
        print(" ".join(letters))
        if whos_step:
            scorePL += 1
        else:
            scoreAI += 1
    whos_step = not whos_step
if scoreAI > scorePL:
    print(f"AI win! {scoreAI} : {scorePL}")
elif scoreAI < scorePL:
    print(f"You win! {scoreAI} : {scorePL}")
else:
    print("We have a tie.")

