line = input()
cnt = 0
while " " not in line:
    lens = int(input())
    if lens == len(line):
        cnt += 1
    line = input()
print(cnt)
