# 앞에서 두번째 부터 데이터의 순서를 보장하기 위해 자신의 위치를 적절한 곳에 삽입
# 시간 복잡도 -> O(n^2)     하지만 데이터가 거의 정렬된 상태면 최선의 경우 O(n)

array = [7,4,5,2,6,8,9,1,3,0]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # start: i부터 ~ end: 0 + 1 까지 -1 씩 감소한다.
        
        if array[j] < array[j-1]:   # 자신보다 큰데이터면 자신과 위치를 바꾼다.(한칸씩 앞당겨짐)
            array[j], array[j-1] = array[j-1], array[j]
        
        else:   # 자신보다 작은데이터를 만나면 멈춤 (왜냐면 자신의 이전 배열을 정렬이 되어 있으니)
            break

print(array)
