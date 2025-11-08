num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

if a == b and b == c and c == a:
    print(3)
elif a == b or b == c or c == a:
    print(2)
elif a != 0 and b != 0 and c != 0:
    print(a * b * c)
else:
    print(c - a)