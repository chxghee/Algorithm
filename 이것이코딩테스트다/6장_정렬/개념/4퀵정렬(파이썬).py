# pivot을 정하고 그것을 기준으로 왼쪽 오른쪽에서 시작하여 큰것 작은것 을 찾아 서로 바꾸는걸 반복 
# 시간복잡도 O(nlogn)            최악의 경우 O(n^2) (데이터가 미리 정렬되어 있을 때)

array = [7,4,5,2,6,8,9,1,3,0]

def quick_sort(array):

    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 왼쪽 분할 부분 (그러니까 피벗보다 작은 수들을 리스트에 넣는다)
    right_side = [x for x in tail if x > pivot] # 오른쪽 분할 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
print(quick_sort(array))