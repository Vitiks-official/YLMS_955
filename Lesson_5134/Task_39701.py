words = input().split()
ml = max(len(i) for i in words)
new_lines = [""] * ml
for i in range(len(words)):
    words[i] += " " * (ml - len(words[i]))
for i in words:
    for j in range(len(i)):
        new_lines[j] += i[j]
for i in range(len(new_lines)):
    if i == 0:
        print("_" + "_".join(list(new_lines[i])) + "_")
    else:
        print(" " + " ".join(list(new_lines[i])) + " ")
print()
for i in range(len(new_lines) - 1, -1, -1):
    if i == 0:
        print("_" + "_".join(list(new_lines[i])) + "_")
    else:
        print(" " + " ".join(list(new_lines[i])) + " ")