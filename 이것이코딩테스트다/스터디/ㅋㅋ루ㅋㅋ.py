# https://www.acmicpc.net/problem/20442

import sys
input = sys.stdin.readline

def count_left_K(st, idx):
    count = 0
    for i in range(0, idx, -1):
        if st[i] == 'K':
            count+=1
    return count

def count_right_K(st, idx):
    count = 0
    for i in range(idx+1, len(st)):
        if st[i] == 'K':
            count+=1
    return count





st = list(input().rstrip())

result = int(1e9)

for i in range(len(st)):
    
    local_sum = 0
    
    if st[i] == 'R':
        local_sum += 1

        left_K_count = count_left_K(st, i)
        right_K_count = count_right_K(st, i)
    

        left = i - 1
        right = i + 1
        while left >= 0 and right < len(st):

            if st[left] == 'R' and st[right] == 'R':
                local_sum += 2
                left -= 1
                right += 1 
                continue
            if st[left] == 'R':
                local_sum += 1
                left -= 1
                continue
            if st[right] == 'R':
                local_sum += 1
                right += 1
                continue
            
            # 둘다 K 여야 만 패스 가능
            if st[right] == 'K' and st[left] == 'K':
                local_sum += 2
                left -= 1
                right += 1 
                continue



