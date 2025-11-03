# https://www.acmicpc.net/problem/14713
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
parrots = []

for _ in range(n):
    parrots.append(deque(input().split()))

l = input().split()



for word in l:
    found = False
    
    for q in parrots:
        if q and q[0] == word:
            q.popleft()
            found = True
            break
    
    if not found:
        print("Impossible")
        sys.exit(0)

#아직 단어가 남아 있디면 불가능
for q in parrots:
    
    if q:
        print("Impossible")
        sys.exit(0)

print("Possible")
