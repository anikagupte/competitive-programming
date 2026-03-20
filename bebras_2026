# question 1
temp = int(input())
if temp < 10:
    print('wear a coat')
else:
    print('no coat needed')

# question 2
n = int(input())
if n < 0:
    print('negative')
elif n > 0:
    print('positive')
else:
    print('zero')

# question 3
n = int(input())
for i in range(n, 0, -1):
    print(i)
print(0)

# question 4
p = input()
attempts = 1
while p != 'letmein' and attempts < 3:
    attempts += 1
    p = input()
if p == 'letmein':
    print('access granted')
elif attempts == 3:
    print('access denied')

# question 5
fname = input().lower()
lname = input().lower()
year = input()

username = fname[0] + lname + year[2:]
print(username)

# question 6
s = input().split()
count = 0
for word in s:
    if len(word) >= 4:
        count += 1
print(count)

# question 7
text = input()
ints = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
padlock = ''
for c in text:
    if c in ints:
        padlock += c

print(padlock)

# question 8
n1 = int(input())
n2 = int(input())
sum = 0

for i in range(n1, n2+1):
    if i % 3 == 0:
        sum += i

print(sum)

# question 9
code = input()
ints = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k','l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

if len(code) == 6:
    if code[0] in ints and code[5] in ints:
        if code[1] in chars and code[2] in chars and code[3] in chars and code[4] in chars:
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')
else:
    print('invalid')

# question 10
nums = input().split()
n_nums = len(nums)
if n_nums % 2 == 1:
    print(nums[(n_nums // 2)])
else:
    avg1 = nums[int(n_nums / 2)] 
    avg2 = nums[int((n_nums / 2) - 1)] 
    print(int((int(avg1) + int(avg2)) / 2))
