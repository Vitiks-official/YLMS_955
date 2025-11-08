side = float(input())
speed = float(input())
num = 0
lock = 0
while True:
    if int(side * 100) / 100 <= speed:
        print(num)
        break
    if side >= speed:
        side0 = side - speed
        side = (side0 ** 2 + speed ** 2) ** 0.5
        num += 1
        lock = 1