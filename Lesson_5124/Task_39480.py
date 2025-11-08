word = word1 = input()
win = "Первый"
while word1 != "" and len(word1) >= len(word):
    word, word1 = word1, word
    if win == "Второй":
        win = "Первый"
    elif win == "Первый":
        win = "Второй"
    word1 = input()
print(win)