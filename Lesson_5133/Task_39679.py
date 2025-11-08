n = int(input())
lines = [input() for i in range(n)]
for i in range(n - 1):
    if lines[i][-1] < lines[i + 1][-1]:
        print((i + 1, lines[i][:-2]))