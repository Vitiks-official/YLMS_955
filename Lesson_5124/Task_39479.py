a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a = a1 * b2 - a2 * b1
b = b1 * b2
some = 2
while some <= a and some <= b:
    if a % some == 0 and b % some == 0:
        a //= some
        b //= some
    else:
        some += 1
print(f"{a}/{b}")