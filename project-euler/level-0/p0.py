# finally got around to making an official account!!

sum = 0

for i in range(1, 795000):
    square = i ** 2
    if square % 2 == 1:
        sum += square

print(sum)
