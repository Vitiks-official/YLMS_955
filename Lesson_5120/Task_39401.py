first = input()
second = input()
third = input()
if first < second:
	first, second = second, first
if second < third:
	second, third = third, second
if first < second:
	first, second = second, first
print(first + ", " + second + ", " + third + ".")