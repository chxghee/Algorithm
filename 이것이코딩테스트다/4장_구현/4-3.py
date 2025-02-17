n = input()
row = int(n[1])
col = int(ord(n[0]) - ord('a')) + 1
count = 0

# 나이트 움직이는 경우의 수
moves = [[-2, 1],[-2,-1],[1,-2],[-1,-2],[2,-1],[2,1],[1,2],[-1,2]]

for move in moves:
    if col + move[0] >= 1 and  col + move[0] <=8 and row + move[1] >=1 and row + move[1] <= 8:
        count += 1

print(count)