fib0 = 2
fib1 = 3
sum = fib0

while fib1 <= 4000000:
    if fib1 % 2 == 0:
        sum += fib1
    temp = fib1
    fib1 += fib0
    fib0 = temp

print(sum)
