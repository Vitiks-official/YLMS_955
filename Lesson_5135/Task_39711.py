line = input()
d = dict()
for i in range(1, len(line) // 2 + 1):
    for j in range(0, len(line) - i + 1):
        if line[j:j + i] not in d:
            d[line[j:j + i]] = 1
        else:
            d[line[j:j + i]] += 1
for i in d:
    if d[i] > 1:
        print(f"{i}: {d[i]}")
