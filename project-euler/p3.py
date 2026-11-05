def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

found = False
j = 600851475143

while not found:
    if 600851475143 % j == 0 and is_prime(j):
        found = True
    else:
        j -= 1

print(j)
