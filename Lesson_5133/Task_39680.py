words = [input() for i in range(int(input()))]
for i in range(len(words)):
    for j in range(1, len(words[i])):
        if words[i][j] < words[i][j - 1]:
            print((i, j))