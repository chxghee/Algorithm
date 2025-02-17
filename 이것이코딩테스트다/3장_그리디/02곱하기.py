import sys

st = list(sys.stdin.readline().rstrip())
numbers = list(map(int, st))

# 다른 방법
# num = [int(x) for x in st]

result = 0

for x in numbers:
    
    if x <= 1 or result <= 1:
        result += x
    else:
        result *= x
    

print(result)