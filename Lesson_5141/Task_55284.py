str1 = input()
str2 = input()
num = int(input())
if len(str1) < num:
    if len(str2) < num:
        print(max(str1, str2))
        print(min(str1, str2))
    else:
        print(str1)
else:
    if len(str2) < num:
        print(str2)
    else:
        print(num)
