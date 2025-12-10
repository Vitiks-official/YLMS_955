line = input()
light = int(input())
if light > 100:
    while line.find("0000") != -1:
        line = line[:line.find("0000")] + "|||" + line[line.find("0000") + 4:]
else:
    for i in range(3):
        if line.find("|||") != -1:
            line = line[:line.find("|||")] + "00" + line[line.find("|||") + 3:]
if line.find("|0|") != -1:
    line = line[:line.find("|0|")] + "|00|" + line[line.find("|0|") + 3:]
print(line)