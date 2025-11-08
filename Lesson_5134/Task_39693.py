k, n, line = input().split(" ")
n = int(n)
print(k[::-1].join([i for i in line.split(k) if len(set(i)) >= n]))