n = input()
print("\n".join([str(n[i:-i]) if i != 0 else str(n) for i in range(len(n) // 2 + len(n) % 2)]))