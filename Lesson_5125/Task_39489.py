k, b = int(input()), int(input())
a = 0
d = 0
c = 0
x = input()
while x != "END":
    y = int(input())
    if y == k * int(x) + b:
        c += 1
    elif y < k * int(x) + b:
        d += 1
    else:
        a += 1
    x = input()
if a != 0:
    print(f"Выше прямой: {a}")
if d != 0:
    print(f"Ниже прямой: {d}")
if c != 0:
    print(f"На прямой: {c}")