text = input()
if "лилипут" in text or "Лилипут" in text or "ЛИЛИПУТ" in text:
	a = 1
else:
	a = 2
if "великан" in text or "Великан" in text or "ВЕЛИКАН" in text:
	b = 1
else:
	b = 2
if a == b:
	print("Я совсем запутался.")
elif a == 1 and b == 2:
	print("В Лилипутии.")
elif a == 2 and b == 1:
	print("В Великании.")