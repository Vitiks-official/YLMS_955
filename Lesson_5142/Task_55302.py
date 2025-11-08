line1 = len(input())
line2 = len(input())
n = int(input())
if line1 > line2:
    line2, line1 = line1, line2
for i in range(line1, line2, n):
    print(i, end=" ")