line = input()
if len(line) <= 7 and "нота" not in line:
    if "до" in line or "ля" in line or "соль" in line:
        if ("до" in line or "ля" in line) and len(line) % 2 == 0 or "соль" in line and len(line) % 2 == 1:
            if line <= "флейта":
                print("МОЖЕТ")
            else:
                print("НЕ МОЖЕТ")
        else:
            print("НЕ МОЖЕТ")
    else:
        if line <= "флейта":
            print("МОЖЕТ")
        else:
            print("НЕ МОЖЕТ")
else:
    print("НЕ МОЖЕТ")