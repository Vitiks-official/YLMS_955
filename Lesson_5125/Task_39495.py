first = 0
second = 0
n = int(input())
i = 1
while i <= n:
    first += i * i
    second += i
    i += 1
second *= second
print(second - first)