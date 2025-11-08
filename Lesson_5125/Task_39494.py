v = int(input())
perc = v * 0.02
r = int(input())
if v - r * perc < v / 2:
    print(v / 2)
else:
    print(float(v - r * perc))