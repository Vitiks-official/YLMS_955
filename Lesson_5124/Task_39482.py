a = int(input())
times = int(input())
a = a * a
while times > 0:
    a /= 2
    times -= 1
print(a)