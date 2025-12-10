symb = input()
nl = []
line = input().upper().split()
for i in line:
    nl.append(f"{symb}".join(list(i)))
print(" ".join(nl))
