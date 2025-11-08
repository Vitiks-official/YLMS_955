sera = int(input())
rtut = sera * 2
nash = sera / 8
sera /= 3
start = sera + rtut + nash
h = 0
while sera + rtut + nash >= start / 2:
    h += 1
    rtut *= 0.99
    nash *= 0.995
print(h, sera + rtut + nash)