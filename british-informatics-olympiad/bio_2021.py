# Q1

def is_pat(input_pat):
    if len(input_pat) == 1: return 'YES'
    for i in range(len(input_pat)):
        temp1 = input_pat[:i]
        temp2 = input_pat[i:]
        if temp1 and temp2:
            if min(temp1) > max(temp2) and is_pat(temp1[::-1]) and is_pat(temp2[::-1]):
                return 'YES'     
    return 'NO'
    
p1, p2 = input().split()
p3 = p1 + p2

print(is_pat(p1))
print(is_pat(p2))
print(is_pat(p3))

# GRADER: 15/21
