def is_prime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

count = 0
i = 2
while count < 10001:
    if is_prime(i):
        count += 1
    i += 1

print(i-1)
