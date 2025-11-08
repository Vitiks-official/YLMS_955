num = float(input())
cnt = 0
s = 0
while num != 0:
    s += num
    cnt += 1
    num = float(input())
print(s / cnt)
