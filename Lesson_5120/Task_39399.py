first = input()
second = input()
if first != "" and second != "":
	if first < second:
		print(first * 5)
	else:
		print(second * 5)
else:
	print("Пусто!")