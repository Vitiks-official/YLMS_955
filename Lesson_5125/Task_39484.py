num = int(input())
a, b = 1, 1
cnt = 2
while b < num:
    a, b = b, a + b
    cnt += 1
if b == num:
    print(cnt)
else:
    print("НЕТ")