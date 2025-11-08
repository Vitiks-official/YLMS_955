new_line = line = input()
while new_line != "":
    if 100 <= len(new_line) < 1000:
        print(line)
    elif len(new_line) % 2 == 0:
        print(new_line * 2)
    elif len(new_line) % 3 == 0:
        print(new_line * 3)
    else:
        print(new_line)
    line = new_line
    new_line = input()