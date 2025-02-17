import sys


n,x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

def binary_left(start, end , target):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if data[mid] == target:
        if mid == 0:
            return mid
        if data[mid-1] != target:
            return mid
        
        return binary_left(start, mid-1, target)
        
    elif data[mid] > target:
        return binary_left(start, mid-1, target)
    else:
        return binary_left(mid+1, end, target)

def binary_right(start, end , target):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if data[mid] == target:
        if mid == n-1:
            return mid
        if data[mid+1] != target:
            return mid
        
        return binary_right(mid+1, end, target)
        


    elif data[mid] > target:
        return binary_right(start, mid-1, target)
    else:
        return binary_right(mid+1, end, target)



start = binary_left(0,n-1,x)
if start == None:
    print(-1)
else:
    
    end = binary_right(0,n-1,x) + 1
    result = end - start
    print(result)
