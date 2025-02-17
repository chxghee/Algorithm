
# 1. sorted() 함수 -> 합병정렬 기반 O(nlogn) 최악의 경우에도 (퀵보단 느리긴 함)
array = [7,4,5,2,6,8,9,1,3,0]

result = sorted(array)
print(result)

# 2. sort() 함수

array.sort()
print(array)


# 3. key: 정렬기준 잡기 -> 함수를 이용한다. 
# 어느 튜플을 정렬할때 좋음

array = [('banan', 2), ('apple', 19), ('carrot', -2)]
def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# 정렬문제 팁
# 1. 별도의 요구사항 없으면 빠르게 라이브러리 쓰기
# 2. 데이터 범위가 한정되어 있으면 계수정렬 쓰기