# Q1

letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
           "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

l1, l2, n = input().split(' ')
n = int(n)

def next_letter(l1 ,l2):
    n1 = letters[l1]
    n2 = letters[l2]
    total = n1 + n2
    if total > 26:
        total = total - 26
    return letter_list[total-1]

if n > 2:
    for i in range(n-2):
        temp = next_letter(l1, l2)
        l1 = l2
        l2 = temp
    print(l2, end="")
elif n == 2:
    print(l2)
else:
    print(l1)

# GRADER: 24/24
