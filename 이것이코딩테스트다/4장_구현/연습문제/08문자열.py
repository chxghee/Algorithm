import sys

st = list(sys.stdin.readline().rstrip())

l = []
num=0
for x in st:
    if x.isalpha():
        l.append(x)
    else:
        num += int(x)

l.sort()

if num != 0:
    l.append(str(num))

print(''.join(l))
