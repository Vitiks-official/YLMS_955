first = input()
second = input()
num = int(input())
if first == "A" and second == "B" or first == "B" and second == "A":
    print("NOT TO GO")
elif first == "A" or second == "A":
    num -= 5
    print(num // 2)
elif first == "B" or second == "B":
    num -= 3
    print(num // 2)
else:
    print("NOT TO GO")