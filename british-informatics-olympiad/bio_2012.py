# Q1

def check_prime(check_num):
    prime = True
    for i in range(2, check_num-1):
        if check_num % i == 0:
            prime = False
    return prime

def prime_factorisation(num):
    primes = []
    for i in range(2, num+1):
        if num % i == 0 and check_prime(i):
            if i not in primes:
                primes.append(i)
    return primes

prime_factors = prime_factorisation(int(input()))

product = 1
for d in prime_factors:
    product *= d

print(product)

# correct but time limited exceeded
