def is_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-1-i]:
            return False
    return True

palindrome = 0

found = False
for j in range(999, 99, -1):
    for i in range(999, 99, -1):
        product = i * j
        if is_palindrome(product):
            if product > palindrome:
                palindrome = product

print(palindrome)
