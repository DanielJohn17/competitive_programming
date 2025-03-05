t = int(input())

def solution():
    word = str(input())

    if len(word) > 10:
        first_element = word[0]
        last_element = word[-1]

        return f"{first_element}{len(word[1:-1])}{last_element}"
    else:
        return word

for _ in range(t):
    print(solution())