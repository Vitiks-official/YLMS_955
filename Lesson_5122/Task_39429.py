name = input()
d = int(input())
if name == "пенс":
    d *= 4
a = d // 960
d %= 960
b = d // 48
d %= 48
c = d // 4
d %= 4
if a != 0:
    print("Фунтов: " + str(a))
if b != 0:
    print("Шиллингов: " + str(b))
if c != 0:
    print("Пенсов: " + str(c))
if d != 0:
    print("Фартингов: " + str(d))

