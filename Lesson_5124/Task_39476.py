line = input()
cnt = 0
cnta = 0
while line != "":
    cnta += 1
    if line == "да":
        cnt += 1
    line = input()
if cnt / cnta >= 0.8:
    print("Достигли")
else:
    print("Пока нет")
