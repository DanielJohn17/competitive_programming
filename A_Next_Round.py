fisrst_line =[int(i) for i in input().split(' ')]
scores = [int(i) for i in input().split(' ')]

n, k = fisrst_line[0], fisrst_line[1]
total_passed = 0
cutoff = scores[k - 1]

for score in scores:
    if score >= cutoff and score > 0:
        total_passed += 1

print(total_passed)
