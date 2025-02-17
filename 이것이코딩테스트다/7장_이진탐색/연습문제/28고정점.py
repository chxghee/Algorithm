import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

def binary_search(start, end):

    if start > end:
        return -1
    mid = end - start

    if data[mid] == mid:
        return mid
    elif data[mid] > mid:
        return binary_search(start, mid-1)
        
    else:
        return binary_search(mid+1, end)
    


print(binary_search(0,n-1))