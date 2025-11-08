ans = [(0, 1)]
for i in range(int(input())):
    if i + 1 == 1:
        ans.append((i + 1, i + 1))
    else:
        ans.append((i + 1, ans[-2][1] * (i + 1)))
print(ans)