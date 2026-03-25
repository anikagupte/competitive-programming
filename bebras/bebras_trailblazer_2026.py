# question 1
n1 = int(input())
n2 = int(input())
sum = 0

for i in range(n1, n2+1):
    if i % 3 == 0:
        sum += i

print(sum)

# marks: 4/4

# question 2
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

# marks: 4/4

# question 3
nums = input().split()
n_nums = len(nums)
if n_nums % 2 == 1:
    print(nums[(n_nums // 2)])
else:
    avg1 = nums[int(n_nums / 2)] 
    avg2 = nums[int((n_nums / 2) - 1)] 
    print(int((int(avg1) + int(avg2)) / 2))

# marks: 4/4

# question 4
# SELECT * FROM Movies WHERE Director="Spielberg" ORDER BY Year DESC, MovieID DESC

# question 5
n = int(input())
finished = False
count = 0

while not finished and n!= 1:
    if n % 2 == 0:
        n = n/2
        count += 1
    else:
        n = (n+1)/2
        count += 1

print(count)

# score: 3/4

# question 6
def encrypt(word):
    
    odd = ""
    even = ""
    for i in range(len(word)):
        if i % 2 == 0:
            odd += word[i]
        else:
            even += word[i]

    for j in range(len(even)-1, -1, -1):
        odd += even[j]

    return odd

w = input()
count = 0
wEnc = encrypt(w)
count += 1
while w != wEnc:
    wEnc = encrypt(wEnc)
    count += 1
print(count)

# marks: 4/4

# question 8
diffs = []
sequence = input().split()
currentDiff = int(sequence[1]) - int(sequence[0])
count = 0

for i in range(len(sequence)-1):
    if int(sequence[i+1]) - int(sequence[i]) == currentDiff:
        count += 1
        print(currentDiff)
    else:
        diffs.append(count)
        currentDiff = int(sequence[i+1]) - int(sequence[i])
        count = 1
        print(currentDiff)
        print(f'count: {count}')

highest = diffs[0]
print(diffs)
for n in diffs:
    if n > highest:
        highest = n

highest += 1
print(highest)

# score: 4/8

# question 9
k = int(input())
string = input()
strings = []

for i in range(0, len(string), k):
    new = ''
    for j in range(k):
        new += string[i+j]
    strings.append[new]

final = []
for s in string:
    new = ''
    for i in range(len(s)-1):
        new += s[i+1]
    new += s[0]
    final.append(new)

newstring = ''
for word in final:
    newstring += word

print(word)
