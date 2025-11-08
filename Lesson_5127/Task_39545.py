legs = 0
hobot = 0
tails = 0
ears = 0
eyes = 0
mouths = 0
while True:
    n = int(input())
    line = input()
    if line == "ОБЕД":
        break
    elif line == "нога":
        legs += n
    elif line == "рот":
        mouths += n
    elif line == "хобот":
        hobot += n
    elif line == "ухо":
        ears += n
    elif line == "глаз":
        eyes += n
    elif line == "хвост":
        tails += n
    else:
        continue
    if min(legs // 4, mouths, hobot, ears // 2, eyes // 2, tails) != 0:
        break
if min(legs // 4, mouths, hobot, ears // 2, eyes // 2, tails) == 0:
    print("Какие-то слоны нецелые. Пошли обедать.")
else:
    print("Есть слон!")
    print(min(legs // 4, mouths, hobot, ears // 2, eyes // 2, tails))

