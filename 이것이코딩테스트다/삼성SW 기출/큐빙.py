def solve():
    def rotate_face_clockwise(face):
        """면을 시계방향으로 90도 회전"""
        return [[face[2-j][i] for j in range(3)] for i in range(3)]
    
    def rotate_face_counterclockwise(face):
        """면을 반시계방향으로 90도 회전"""
        return [[face[j][2-i] for j in range(3)] for i in range(3)]
    
    def rotate_cube(cube, direction):
        """큐브를 주어진 방향으로 회전"""
        # 큐브 면 순서: U(위), D(아래), F(앞), B(뒤), L(왼쪽), R(오른쪽)
        U, D, F, B, L, R = cube
        
        if direction == "U+":  # 위 면 시계방향
            cube[0] = rotate_face_clockwise(U)
            # 인접면 회전: F->R->B->L->F
            temp = [F[0][i] for i in range(3)]
            for i in range(3):
                F[0][i] = R[0][i]
                R[0][i] = B[0][i]
                B[0][i] = L[0][i]
                L[0][i] = temp[i]
                
        elif direction == "U-":  # 위 면 반시계방향
            cube[0] = rotate_face_counterclockwise(U)
            # 인접면 회전: F->L->B->R->F
            temp = [F[0][i] for i in range(3)]
            for i in range(3):
                F[0][i] = L[0][i]
                L[0][i] = B[0][i]
                B[0][i] = R[0][i]
                R[0][i] = temp[i]
                
        elif direction == "D+":  # 아래 면 시계방향
            cube[1] = rotate_face_clockwise(D)
            # 인접면 회전: F->L->B->R->F
            temp = [F[2][i] for i in range(3)]
            for i in range(3):
                F[2][i] = L[2][i]
                L[2][i] = B[2][i]
                B[2][i] = R[2][i]
                R[2][i] = temp[i]
                
        elif direction == "D-":  # 아래 면 반시계방향
            cube[1] = rotate_face_counterclockwise(D)
            # 인접면 회전: F->R->B->L->F
            temp = [F[2][i] for i in range(3)]
            for i in range(3):
                F[2][i] = R[2][i]
                R[2][i] = B[2][i]
                B[2][i] = L[2][i]
                L[2][i] = temp[i]
                
        elif direction == "F+":  # 앞 면 시계방향
            cube[2] = rotate_face_clockwise(F)
            # 인접면 회전: U->R->D->L->U
            temp = [U[2][i] for i in range(3)]
            for i in range(3):
                U[2][i] = L[2-i][2]
                L[2-i][2] = D[0][2-i]
                D[0][2-i] = R[i][0]
                R[i][0] = temp[i]
                
        elif direction == "F-":  # 앞 면 반시계방향
            cube[2] = rotate_face_counterclockwise(F)
            # 인접면 회전: U->L->D->R->U
            temp = [U[2][i] for i in range(3)]
            for i in range(3):
                U[2][i] = R[i][0]
                R[i][0] = D[0][2-i]
                D[0][2-i] = L[2-i][2]
                L[2-i][2] = temp[i]
                
        elif direction == "B+":  # 뒤 면 시계방향
            cube[3] = rotate_face_clockwise(B)
            # 인접면 회전: U->L->D->R->U
            temp = [U[0][i] for i in range(3)]
            for i in range(3):
                U[0][i] = R[i][2]
                R[i][2] = D[2][2-i]
                D[2][2-i] = L[2-i][0]
                L[2-i][0] = temp[i]
                
        elif direction == "B-":  # 뒤 면 반시계방향
            cube[3] = rotate_face_counterclockwise(B)
            # 인접면 회전: U->R->D->L->U
            temp = [U[0][i] for i in range(3)]
            for i in range(3):
                U[0][i] = L[2-i][0]
                L[2-i][0] = D[2][2-i]
                D[2][2-i] = R[i][2]
                R[i][2] = temp[i]
                
        elif direction == "L+":  # 왼쪽 면 시계방향
            cube[4] = rotate_face_clockwise(L)
            # 인접면 회전: U->F->D->B->U
            temp = [U[i][0] for i in range(3)]
            for i in range(3):
                U[i][0] = B[2-i][2]
                B[2-i][2] = D[i][0]
                D[i][0] = F[i][0]
                F[i][0] = temp[i]
                
        elif direction == "L-":  # 왼쪽 면 반시계방향
            cube[4] = rotate_face_counterclockwise(L)
            # 인접면 회전: U->B->D->F->U
            temp = [U[i][0] for i in range(3)]
            for i in range(3):
                U[i][0] = F[i][0]
                F[i][0] = D[i][0]
                D[i][0] = B[2-i][2]
                B[2-i][2] = temp[i]
                
        elif direction == "R+":  # 오른쪽 면 시계방향
            cube[5] = rotate_face_clockwise(R)
            # 인접면 회전: U->B->D->F->U
            temp = [U[i][2] for i in range(3)]
            for i in range(3):
                U[i][2] = F[i][2]
                F[i][2] = D[i][2]
                D[i][2] = B[2-i][0]
                B[2-i][0] = temp[i]
                
        elif direction == "R-":  # 오른쪽 면 반시계방향
            cube[5] = rotate_face_counterclockwise(R)
            # 인접면 회전: U->F->D->B->U
            temp = [U[i][2] for i in range(3)]
            for i in range(3):
                U[i][2] = B[2-i][0]
                B[2-i][0] = D[i][2]
                D[i][2] = F[i][2]
                F[i][2] = temp[i]
    
    T = int(input())
    
    for _ in range(T):
        # 큐브 초기화 (맞춰진 상태)
        cube = [
            [['w' for _ in range(3)] for _ in range(3)],  # U (위) - 흰색
            [['y' for _ in range(3)] for _ in range(3)],  # D (아래) - 노란색
            [['r' for _ in range(3)] for _ in range(3)],  # F (앞) - 빨간색
            [['o' for _ in range(3)] for _ in range(3)],  # B (뒤) - 주황색
            [['g' for _ in range(3)] for _ in range(3)],  # L (왼쪽) - 초록색
            [['b' for _ in range(3)] for _ in range(3)]   # R (오른쪽) - 파란색
        ]
        
        n = int(input())
        moves = input().split()
        
        # 각 회전 수행
        for move in moves:
            rotate_cube(cube, move)
        
        # 위 면(U) 출력
        for row in cube[0]:
            print(''.join(row))

solve()