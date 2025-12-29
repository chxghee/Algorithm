from collections import deque
import sys
input = sys.stdin.readline

Q = int(input())
dq = deque()
vertical = False  # False: horizontal, True: vertical
b_count = 0
w_count = 0

def fall():
    global b_count
    # 세로일 때만 발생
    if not vertical:
        return
    # 뒤에서부터 공을 제거, 벽을 첫 발견하면 종료
    while dq and dq[-1] == 'b':
        dq.pop()
        b_count -= 1
    # 벽 만나면 멈춤

for _ in range(Q):
    cmd = input().split()

    if cmd[0] == 'push':
        if cmd[1] == 'b':  # 공 삽입
            if vertical:
                # 세로에서 아래에 벽이 없으면 즉시 떨어짐
                if not dq or all(x == 'b' for x in dq):
                    # 바닥에 벽 없으므로 떨어짐
                    continue
            dq.append('b')
            b_count += 1
            fall()  # 혹시 떨어질 공 반영

        else:  # push w
            dq.append('w')
            w_count += 1

    elif cmd[0] == 'pop':
        if dq:
            x = dq.popleft()
            if x == 'b': b_count -= 1
            else: w_count -= 1
            fall()

    elif cmd[0] == 'rotate':
        # 수직/수평 토글
        vertical = not vertical
        fall()

    elif cmd[0] == 'count':
        if cmd[1] == 'b':
            print(b_count)
        else:
            print(w_count)
