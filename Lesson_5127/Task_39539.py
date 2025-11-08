d, z = 0, 0
while True:
    line = input()
    if line == "":
        break
    elif line == "добрый":
        d += 1
    elif line == "злой":
        z += 1
    elif line == "Какой подарок?":
        if d > z and line1 == "добрый":
            print("серебряный шиллинг")
        elif z > d and line1 == "злой":
            print("золотой")
        else:
            print("Ах, не знаю!")
            break
        d = 0
        z = 0
    line1 = line