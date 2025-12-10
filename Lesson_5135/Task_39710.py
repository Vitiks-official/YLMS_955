line = list(map(int, input().split()))
ind1, ind2 = map(int, input().split())
ind1, ind2 = min(ind1, ind2), max(ind1, ind2)
print(sum(line[ind1:ind2]))