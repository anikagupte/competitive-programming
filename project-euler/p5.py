found = False
i = 20
while not found:
    divisible = True
    count = 1
    while divisible and count < 21:
        if i % count != 0:
            divisible = False
        count += 1
    if divisible:
        found = True
    else:
        i += 20

print(i)
