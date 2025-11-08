grades = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(int(input())):
    for j in range(11):
        count = int(input())
        grades[j][0] += count
        if count != 0:
            grades[j][1] += 1
maxn, minn = 0, 0
for i in range(len(grades)):
    if grades[i][1] != 0:
        aver = grades[i][0] / grades[i][1]
    if aver > grades[maxn][0] / grades[maxn][1]:
        maxn = i
    if aver < grades[minn][0] / grades[minn][1]:
        minn = i
print(minn + 1, maxn + 1)
