import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))
    BB = [B[n] for n in range(N) if A[n] == 0]
    BB.reverse()

    M = int(input())
    C = list(map(int, sys.stdin.readline().strip().split()))
    if (len(BB) >= M) :
        print(*BB[:M])
    elif (len(BB) == 0):
        print(*C[:M])
    else :
        print(*BB, end=' ')
        print(*C[:M - len(BB)])