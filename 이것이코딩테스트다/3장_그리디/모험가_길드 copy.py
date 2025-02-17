import sys

N = int(sys.stdin.readline())
fear = list(map(int, sys.stdin.readline().split()))

fear.sort()
g = 0

i = 0
while i < N:
    if fear[i] == 1:
        g += 1
        i += 1
        continue

    if N-i-1 >= fear[i]:
        g += 1
        i += fear[i]

    else:
        i+= 1


print(g)
