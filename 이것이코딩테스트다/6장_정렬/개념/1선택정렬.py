# 가장 작은 수를 선택해 앞으로 보냄 -> O(n^2)

array = [7,4,5,2,6,8,9,1,3,0]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i] # 이렇게 한줄로 스와핑 할 수 있다

print(array)