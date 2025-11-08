num = int(input())
rad = 1
d = 2
while num >= d:
    if num % d == 0:
        rad *= d
        while num % d == 0:
            num //= d
    d += 1
print(rad)