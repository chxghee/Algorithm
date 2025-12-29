# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


# 홀수의 약수는 홀수 -> 즉 홀수 - 홀수 = 짝수 = 소수가 절대 아님 = 홀수를 넘겨 받은 사람은 무조건 짝수를 주게 되어 있음 -> 즉 패배
# 짝수 라면 -> 2의 거듭제곱이 아니면 약수에 홀 수 포함 -> 홀수를 넘겨 줄 수 있음 -> 즉 이길 수 있음
# -> 2의 거듭제곱이면

def get_power(num):
    cnt = 0

    while num % 2 == 0:
        num //= 2
        cnt += 1

    if num == 1:
        return cnt
    return -1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())

    if n % 2 == 1:  #홀수이먄 밥 승리
        print('B')
    else:
        power = get_power(n)
        if power == -1:
            print('A')
        else:
            if power % 2 == 0:
                print('A')
            else:
                print('B')


