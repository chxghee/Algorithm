import sys


def binary_search(parts, start, end, target):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if parts[mid] == target:
        return "yes"
    elif parts[mid] < target:
        return binary_search(parts, mid+1, end, target)
    else:
        return binary_search(parts, start, mid - 1, target)
    

n = int(sys.stdin.readline().rstrip())
parts = list(map(int, sys.stdin.readline().split()))



m = int(sys.stdin.readline().rstrip())
finds = list(map(int, sys.stdin.readline().split()))

parts.sort()

for find in finds:
    print(binary_search(parts,0,n-1,find), end=' ')
