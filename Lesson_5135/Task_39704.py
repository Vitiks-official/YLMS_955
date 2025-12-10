msgs = []
nm = []
line = input()
while line:
    msgs.append(line)
    line = input()
line = input()
for i in msgs:
    if i[1:].startswith(line):
        nm.append(i[1 + len(line):].lstrip().capitalize())
print("\n".join(sorted(nm)))