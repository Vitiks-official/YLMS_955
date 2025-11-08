star = False
n = 0
while True:
    if not star:
        n += 1
    line = input()
    if "звезд" in line or "Звезд" in line:
        star = True
    if line == "ВСЁ":
        break
if star:
    print(n)
else:
    print("НЕТ")