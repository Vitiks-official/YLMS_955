is_star = False
n_star = 0
n = 0
while True:
    n += 1
    line = input()
    if "звезд" in line or "Звезд" in line:
        is_star = True
        n_star = n
    elif "пал" in line or "пад" in line:
        is_star = False
    if line == "ВСЁ":
        break
if is_star:
    print(n_star)
else:
    print("НЕТ")