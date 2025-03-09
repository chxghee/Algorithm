import sys
input = sys.stdin.readline

def validation(data):
    sop = 0
    for i in range(1, G):
        sop  += data[i]
        if sop > i:
            return False
    return True    



G = int(input())
p = int(input())

data = [0] * (G + 1)

result = 0
for i in range(1, p):
    g = int(input())
    data[g] += 1
    print(data)
    if not validation(data):
        break
    result += 1

print(result)
