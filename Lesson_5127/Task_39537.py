star = False
while True:
    line = input()
    if "звезд" in line or "Звезд" in line:
        star = True
    if line == "ВСЁ":
        break
if star:
    print("Загадывай!")
else:
    print("НЕТ")