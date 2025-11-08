n = int(input())
m = int(input())
k = int(input()) * 12 * 10
maxs = [0, 0]
for i in range(1, k // m + 1):
    if (k - m * i) % n == 0:
        if maxs[0] * 2 + maxs[1] * 5 < i * 5 + (k - m * i) // n * 2 and (k - m * i) // n != 0:
            maxs[0] = (k - m * i) // n
            maxs[1] = i
print(maxs[0] * 2 + maxs[1] * 5)
print((maxs[0], maxs[1]))