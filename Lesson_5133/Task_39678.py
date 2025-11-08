food = []
count = []
for i in range(int(input())):
    order = input()
    if order not in food:
        food.append(order)
        count.append(1)
    else:
        count[food.index(order)] += 1
for i in range(len(food)):
    print((count[i], food[i]))