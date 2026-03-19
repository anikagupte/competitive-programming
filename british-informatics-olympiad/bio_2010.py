# Q1

num = input("anagram number: ")
nums = []
product = 0
product_nums = []
ans = []

def check_is_equal(list1, list2):
    return sorted(list1) == sorted(list2)

for digit in num:
    nums.append(digit)

for i in range(2, 9):
    product = i * int(num)
    for digit in str(product):
        product_nums.append(digit)
    if check_is_equal(nums, product_nums):
        ans.append(i)
    product_nums = []

if len(ans) > 0:
    for n in ans:
        print(n, end=" ")
    print()
else:
    print("NO")

# GRADER: 25/25

# Q3
# b)

# 3 oz | 8 oz
# 1. fill 8 oz jug
# 2. pour into 3 oz jug until full
# 3. empty 3 oz jug
# 4. pour from 8 ox jug into 3 oz jug
# there is 2 oz left in the 8 oz jug

# mark: 2/2

# d)

# no - imagine there are three jugs of 2 oz, 3 oz and 4 oz
# fill the 4 oz jug and pour into the 3 oz jug
# pour the 3 oz jug into the 2 oz jug
# the final jug can never have 1 oz in it, unless its capacity is 1 oz
# this is because pouring will either empty or fill a jug

# mark: 2/5
# markscheme:
# Pouring liquid between two jugs either empties the pourer, fills the recipient, or both.
# Every step (or each of the three operations) either empties or fills at least one jug.
# After each step there must be at least one empty or one full jug.
# There are no 1oz capacity jugs, so a jug containing 1oz is neither full or empty.
# If no jug is empty or full then no sequence of steps will work.
