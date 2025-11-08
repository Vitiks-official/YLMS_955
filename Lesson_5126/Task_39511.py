s = 0
k = 0
for i in input():
    if i == "с":
        s += 1
    elif i == "к":
        k += 1
cnt = 2
cnt += k * 3
cnt -= s * 2
if cnt < 0:
    print(f"1/{10 ** abs(cnt)}")
else:
    print(10 ** cnt)