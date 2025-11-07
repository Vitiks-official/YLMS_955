first = input()
second = input()
symb = input()
if symb == "<":
	if first < second:
		print(first)
	else:
		print(second)
elif symb == ">":
	if first > second:
		print(first)
	else:
		print(second)
else:
	print(first)