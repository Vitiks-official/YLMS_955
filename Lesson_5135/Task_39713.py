line = input().lstrip("%")
symbs = [line[0]]
for i in line[1:]:
    if i == "%":
        symbs[-1] += i
    elif i == symbs[-1][-1]:
        symbs[-1] += i
    else:
        symbs.append(i)
ans = ""
for i in symbs:
    if len(i) == 2:
        if i[0] == i[1]:
            ans += i[0]
    elif len(i) > 1:
        ans += i[0]
print(ans)
