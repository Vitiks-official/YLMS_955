line = list(map(int, input().split()))
ind1, ind2 = map(int, input().split())
print(sum(line[ind1:ind2]))