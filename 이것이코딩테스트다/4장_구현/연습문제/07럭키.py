import sys

n = list(sys.stdin.readline().rstrip())

l = 0
for i in range(0, len(n)//2):
    l += int(n[i])
r = 0
for i in range(len(n)//2, len(n)):
    r += int(n[i])

if r == l:
    print("LUCKY")
else:
    print("READY")


