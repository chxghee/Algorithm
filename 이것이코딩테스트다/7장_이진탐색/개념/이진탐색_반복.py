arr = [1,3,6,7,8,10,15,17,21,33]

def binary_search(arr, start, end, target):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None
    



target = int(input())
result = binary_search(arr, 0, len(arr) -1, target)

if result == None:
    print("없음")
else:
    print("찾은 index:", result )






