r, n, m = int(input()), int(input()), int(input())
s = 0
t = 0
while s < r:
    s += n
    t += 1
    n += m
print(t)