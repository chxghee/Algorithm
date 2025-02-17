import sys
# 집합은 어떤것이 존재 하는지 여부를 알고 싶을때 유용

n = int(sys.stdin.readline().rstrip())
parts = set(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline().rstrip())
finds = list(map(int, sys.stdin.readline().split()))


for find in finds:
    if find in parts:
        print("yes", end=' ')
    else:
        print("no", end=' ')
