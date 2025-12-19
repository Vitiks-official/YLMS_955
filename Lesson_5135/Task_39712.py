line = input()
words = []
no_words = []
for i in line.split():
    w, nw = "", ""
    for j in i:
        if j.isalpha():
            w += j
        else:
            nw += j
    if w:
        words.append(w)
    if nw:
        no_words.append(nw)
print(" ".join(words).title())
print(" ".join(no_words))