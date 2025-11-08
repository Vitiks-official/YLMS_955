h1 = int(input())
h2 = int(input())
h3 = int(input())
h4 = int(input())
h5 = int(input())
maxh = h1
answer = "1"
if h2 > h1:
    answer += " 2"
    maxh = h2
if h3 > h1 and h3 > maxh:
    answer += " 3"
    maxh = h3
if h4 > h1 and h4 > maxh:
    answer += " 4"
    maxh = h4
if h5 > h1 and h5 > maxh:
    answer += " 5"
    maxh = h5
print(answer)