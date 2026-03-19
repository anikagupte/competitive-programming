# question 1
from math import sqrt, trunc

r = int(input())
t = int(input())
y = int(input())
n = int(input())

square = r**2 + t * y * n / 3.14
radius = sqrt(square)
print(trunc(radius))

# test cases passed: 5/5

# question 2
n = int(input())
gen = int(input())
sides = n
for i in range(gen):
    n = sides
    for i in range(n):
        sides += n+1
        print(sides)

print(sides)

# question 3
n = int(input())
bowls = []
for i in range(n):
    bowls.append(int(input()))
bowls.sort(reverse=True)
largest = bowls[0]
height = largest
bowls.remove(largest)
for i in range(len(bowls)-1):
    next = bowls[0]
    if next < largest:
        bowls.remove(next)
        largest = next
    else:
        height += next
        largest = next
        bowls.remove(largest)
print(height)

# test cases passed: 2/10
