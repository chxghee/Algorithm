
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static Queue<Node> devileQ, sooyeonQ;
    static int n, m;
    static Node devileStart, sooyoenStart, angel;
    static boolean[][] sVisited;
    static int[][] map; 
    // 0, 1, 2, 3, 4
    // 빈 공간, 벽, 수연, 여신, 악마 

    public static void main(String[] args) throws IOException {

        int tc = Integer.parseInt(br.readLine());

        for (int t = 1; t <= tc ; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            devileQ = new ArrayDeque<>();
            sooyeonQ = new ArrayDeque<>();

            sVisited = new boolean[n][m];

            map = new int[n][m];
            for (int i = 0; i < n; i++) {
                String input = br.readLine();
                for (int j = 0; j < m; j++) {
                    char c = input.charAt(j);
                    map[i][j] = mapper(c, i, j);
                }
            }

            // 악마를 먼저 퍼뜨리고 
            // 수연을 이동시켜야 겹치지 않도록 이동시킬 수 있음
            int result = bfs();
            String output = result == -1 ? "GAME OVER" : String.valueOf(result);
            sb.append('#').append(t).append(' ').append(output).append('\n');
        }
        System.out.println(sb);
    }

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    
    static int bfs() {

        int time = 1;
        while (!sooyeonQ.isEmpty()) {

            int dcnt = devileQ.size();
            int scnt = sooyeonQ.size();
            // System.out.println("time " + time);

            if (scnt == 0) return -1;

            // 해당 시간동안 악마 넓어지기 
            for (int k = 0; k < dcnt; k++) {
                Node nowDevile = devileQ.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = nowDevile.x + dx[i];
                    int ny = nowDevile.y + dy[i];

                    // 레인지가 아니거나 이미 방문했다면? 
                    if (!inRange(nx, ny) || map[nx][ny] == 4) {
                        continue;
                    }

                    // 벽이거나 여신 지역이면 패스
                    if (map[nx][ny] == 1 || map[nx][ny] == 3) continue;

                    devileQ.offer(new Node(nx, ny, 4));
                    map[nx][ny] = 4; //  악마는 맵에 칠해 버림 
                }
            }

            // 수연 이동 
            for (int k = 0; k < scnt; k++) {
                Node nowSooyeon = sooyeonQ.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = nowSooyeon.x + dx[i];
                    int ny = nowSooyeon.y + dy[i];

                    if (!inRange(nx, ny)) continue;

                    // 수연이 여신 도착 하면 종료
                    if (map[nx][ny] == 3) return time;
                    
                    // 빈 공간이 아니라면?  ?
                    if (map[nx][ny] != 0 || sVisited[nx][ny]) {
                        continue;
                    }
                    
                    sooyeonQ.offer(new Node(nx, ny, 2));
                    sVisited[nx][ny] = true;
                }
            }

            time++;

            // printMap();
        }

        // 만약 도착 못하면 
        return -1;
    }

    static void printMap() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(" " + map[i][j]);
            }
            System.out.println();
        }
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < m);
    }

    static int mapper(char c, int x, int y) {
        switch (c) {
            case '.':
                return 0;

            case 'X':
                return 1;

            case 'S':
                sooyeonQ.offer(new Node(x, y,2));
                sVisited[x][y] = true;
                return 2;
        
            case 'D':
                angel = new Node(x, y, 3);
                return 3;
        
            case '*':
                devileQ.offer(new Node(x, y, 4));
                return 4;
        }
        return 0;
    }

    
}

class Node {
    int x, y, type;

    public Node(int x, int y, int type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }
}
