num = int(input())
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a == 0 and b == 0 and c == 0:
    print(d * 1000)
elif a == 0 and b == 0:
    print(c * 1000 + d)
elif a == 0:
    print(b * 1000 + c * 10 + d)
else:
    print(a * 1000 + b * 100 + c * 10 + d)