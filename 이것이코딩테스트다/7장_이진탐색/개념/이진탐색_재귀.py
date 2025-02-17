arr = [1,3,6,7,8,10,15,17,21,33]

def binary_search(arr, start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, end, target)
    
    else:
        return binary_search(arr, start, mid-1, target)


target = int(input())
result = binary_search(arr, 0, len(arr) -1, target)

if result == None:
    print("없음")
else:
    print("찾은 위치:", result )






