line = input()
rot = 0
x, y = 0, 0
while line != "СТОП":
    if line == "налево":
        rot = (rot + 3) % 4
    elif line == "направо":
        rot = (rot + 1) % 4
    elif line == "шаг":
        if rot == 0:
            y += 1
        elif rot == 1:
            x += 1
        elif rot == 2:
            y -= 1
        else:
            x -= 1
    line = input()
print(x, y)
