str1 = input()
str2 = input()
str3 = input()
main = input()
len_sum = 0
cnt = 0
if str1 in main:
    len_sum += len(str1)
    cnt += 1
if str2 in main:
    len_sum += len(str2)
    cnt += 1
if str3 in main:
    len_sum += len(str3)
    cnt += 1
if cnt != 0:
    len_sum /= cnt
    print((len_sum / len(main) + 1) * 42)
else:
    print(0)
