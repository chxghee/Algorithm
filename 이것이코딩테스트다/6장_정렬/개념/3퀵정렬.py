# pivot을 정하고 그것을 기준으로 왼쪽 오른쪽에서 시작하여 큰것 작은것 을 찾아 서로 바꾸는걸 반복 
# 시간복잡도 O(nlogn)
array = [7,4,5,2,6,8,9,1,3,0]

def quick_sort(array, start, end):
    
    # base case 파티션의 원소가 1개면 종료
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while  left <= right:   # 양 옆에서 출발한게 만나면 (그러니까 만날때 까지 반복)

        # 왼쪽에서 pivot보다 큰 첫 데이터를 찾을때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:    # 만약 만나서 엇갈렸다면 -> 피벗과 작은 수를 교환
            array[right], array[pivot] = array[pivot],  array[right]
    
        else:               # 만나지 않으면 -> 작은수 큰수 교환
            array[left], array[right] = array[right], array[left]

    # right가 기준인 이유는 결국 pivot은 작은 수와 바뀌니까 오른쪽의 인덱스와 피벗 위치가 같게 된다.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)
print(array)

