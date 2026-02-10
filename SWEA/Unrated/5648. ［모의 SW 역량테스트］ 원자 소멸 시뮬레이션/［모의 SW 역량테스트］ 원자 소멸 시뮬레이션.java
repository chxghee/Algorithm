import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Solution {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    
    static int N, result, leftcount = 0;
    static Atom[] atoms;
    static int[][] map = new int[4002][4002];
    
    public static void main(String[] args) throws IOException {

        int tc = nextInt();

        for (int t = 1; t <= tc; t++) {
            N = nextInt();

            result = leftcount = 0;
            atoms = new Atom[N];
            for (int j = 0; j < N; j++) {
                atoms[j] = new Atom(nextInt(), nextInt(), nextInt(), nextInt());
            }

            for (int time = 0; time < 4002; time++) {

                if (leftcount == N) break;

                // 1. 일단 모든 원자들 움직이기
                for (int i = 0; i < N; i++) {
                    if (atoms[i] == null) continue;

                    atoms[i].move();    
                    if (!atoms[i].check()) {   // 맵 밖으로 나가면 삭제
                        atoms[i] = null; 
                        leftcount++;
                        continue;
                    }

                    map[atoms[i].y][atoms[i].x]++;
                }


                // 2. 충돌 처리 (같은 좌표에 2개 이상 있는 경우)
                for (int i = 0; i < N; i++) {
                    if (atoms[i] == null) continue;

                    int x = atoms[i].x;
                    int y = atoms[i].y;

                    if (map[y][x] >= 2) {
                        result += atoms[i].k;
                        atoms[i].isDead = true;
                        leftcount++;
                    }
                    
                }

                // 3. 맵 청소 - 죽은 원자 삭제, 맵 다시 초기화
                for (int i = 0; i < N; i++) {
                    if (atoms[i] == null) continue;
                    int x = atoms[i].x;
                    int y = atoms[i].y;

                    if (atoms[i].isDead) {
                        atoms[i] = null;
                    }
                    map[y][x] = 0;
                }
            }

            sb.append("#").append(t)
            .append(" ").append(result).append("\n");
        }

        System.out.println(sb.toString());
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}

class Atom {

    static int[] dx = {0,0,-1,1};   // 상 하 좌 우
    static int[] dy = {1,-1,0,0};

    int x, y, dir, k;
    boolean isDead = false;

    public Atom(int a, int b, int dir, int k) {
        x = (a + 1000) * 2; // 0.5초를 다루기 위해 2배로 맵 늘리기
        y = (b + 1000) * 2;
        this.dir = dir;
        this.k = k;
    }

    public void move() {   
        this.x += dx[dir];
        this.y += dy[dir];
    }

    public boolean isSamePosition(Atom atom) {
        return this.x == atom.x && this.y == atom.y;
    }

    public boolean isSamePosition(int a, int b) {
        return this.x == a && this.y == b;
    }

    public boolean check() {
        return (0 <= this.x && this.x <= 4000) && (0 <= this.y && this.y <= 4000); 
    }
}

