lines = []
line = input()
while line != "разбитое корыто":
    lines.append(line)
    line = input()
for i in range(len(lines) - 1):
    for j in range(len(lines) - i - 1):
        if len(lines[j]) > len(lines[j + 1]):
            lines[j], lines[j + 1] = lines[j + 1], lines[j]
for i in lines:
    print(i)