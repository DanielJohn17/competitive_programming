n = int(input())
x = 0


for i in range(n):
    op = str(input())

    if op == "++X" or op == "X++":
        x += 1
    else:
        x -= 1


print(x)
