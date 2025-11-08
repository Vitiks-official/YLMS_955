fish = []
name = input()
while name:
    fish.append(name)
    name = input()
fish1 = fish[::]
for i in range(len(fish) - 1):
    for j in range(len(fish) - i - 1):
        if fish[j] > fish[j + 1]:
            fish[j], fish[j + 1] = fish[j + 1], fish[j]
for i in range(len(fish1) - 1):
    for j in range(len(fish1) - i - 1):
        if len(fish1[j]) > len(fish1[j + 1]):
            fish1[j], fish1[j + 1] = fish1[j + 1], fish1[j]
if fish == fish1:
    print("YES")
else:
    for i in range(len(fish)):
        if fish[i] != fish1[i]:
            print(fish[i], fish1[i])
            break