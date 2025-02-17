
# 1. 재귀를 이용한 간단한 피보나치 수열 -> O(2^n)
def fibo1(x):
    if x == 1 or x == 2:
        return 1
    return fibo1(x-1) + fibo1(x-2)

# 문제점 -> 중복호출이 발생할 수 있다.
# 예를 들어 6을 입력하면 fibo(3)가 3번 중복되어 호출이 된다.

# 2. 재귀 DP로(top-down) 리팩토링한 피보나치 수열 (메모이제이션) -> O(n)

# 2-1 우선 계산 결과를 저장할 배열 초기화 (메모장)
d = [0] * 100

def fibo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:       # 메모장에 값이 저장되어 있다면 -> 다시 함수를 호출하지 않고 메모장의 값을 리턴
        return d[x]
    
    d[x] = fibo2(x-1) + fibo2(x-2)  # 메모장에 값이 없으면 계산해서 호출
    return d[x]


# 3. 반복문 DP로(bottom-up)  리팩토링한 피보나치 수열 (DP테이블) -> O(n)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n - 1):
    d[i] = d[i-1] - d[i-2]

