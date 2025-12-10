n = int(input())
stack = []
ans = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        ans.append(str(i))
        if i != n // i:
            stack.append(str(n // i))
ans.extend(stack[::-1])
print(" ".join(ans))