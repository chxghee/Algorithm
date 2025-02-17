def dfs_combinations(arr, r, start, path, result):
    # 조합의 길이가 r이 되면 결과에 추가
    if len(path) == r:
        result.append(path[:])  # 깊은 복사로 결과 저장 (path[:]로 복사히면, result를 변경해도 path가 변경되지 않음)
        return

    # DFS로 조합 생성
    for i in range(start, len(arr)):
        # 현재 원소 선택
        path.append(arr[i])
        
        # 다음 DFS 호출 (i + 1로 진행하여 중복 방지)
        dfs_combinations(arr, r, i + 1, path, result)
        
        # 선택 해제 (백트래킹)
        path.pop()

# 조합 호출
arr = [1, 2, 3, 4]
r = 2
result = []
dfs_combinations(arr, r, 0, [], result)

print(result)