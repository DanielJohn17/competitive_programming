t = int(input())
total = 0

def solution():
    certainties = input().split(' ')

    if sum(int(i) for i in certainties) >= 2:
        return 1
    return 0


for _ in range(t):
    total += solution()

print(total)
