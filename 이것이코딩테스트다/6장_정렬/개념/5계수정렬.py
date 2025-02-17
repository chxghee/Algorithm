# 정렬할 값들의 범위만큼 배열을 선언하여 해당 인덱스에 등장횟수를 저장한 다음 출력하는 것
# 시간 복잡도 O(n + k)  k: 가장 큰 수

# 활용: 데이터의 크기가 적당이 한정 되어 있고, 여러 중복값이 존재할 때 활용하면 좋다.

array = [7,5,9,0,3,1,6,2,9,1,4,11,0,5,2]

count = [0] * (max(array) + 1)      # 0도 포함해야 해서 한칸 더 크게 만듬

for i in range(len(array)):
    count[array[i]] += 1

result = []
for i in range(len(count)):
    for j in range(count[i]):
        result.append(i)

print(result)

