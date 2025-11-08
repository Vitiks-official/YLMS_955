str1 = input()
str2 = input()
str3 = input()
if len(str1) > len(str2):
    str1, str2 = str2, str1
if len(str2) > len(str3):
    str2, str3 = str3, str2
if len(str1) > len(str2):
    str1, str2 = str2, str1
if len(str1) == len(str2):
    str2, str1 = max(str1, str2), min(str1, str2)
if len(str2) == len(str3):
    str3, str2 = max(str2, str3), min(str2, str3)
if len(str1) == len(str2):
    str2, str1 = max(str1, str2), min(str1, str2)
print(str1)
print(str2)
print(str3)