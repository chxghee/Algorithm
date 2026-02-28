
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static int n, cnt = 2;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = nextInt();
            }
        }

        // 우선 섬 그루핑
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) bfs(i, j);
            }
        }

        int result = multiBfs();
        System.out.println(result);
    }


    static Queue<Node> offerEdge(int[][] owner) {
        Queue<Node> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] != 0 && isAdjSea(i, j))  {
                    q.offer(new Node(i, j, map[i][j]));
                    owner[i][j] = map[i][j];
                }
            }
        }

        return q;
    }

    static boolean isAdjSea(int x, int y) {
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (inRange(nx, ny) && map[nx][ny] == 0) {
                return true;
            }
        }
        return false;
    }
    


    static int multiBfs() {
        
        int result = Integer.MAX_VALUE;
        int[][] dist = new int[n][n];
        int[][] owner = new int[n][n];

        Queue<Node> q = offerEdge(owner);

        while (!q.isEmpty()) {
            Node now = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                
                if (!inRange(nx, ny)) continue;
                
                if (map[nx][ny] != 0) continue;

                // 내가 펼치는 칸을 방문 했을때 
                if (owner[nx][ny] == now.island) continue;

                // 첫방문
                if (owner[nx][ny] == 0) {
                    dist[nx][ny] = dist[now.x][now.y] + 1;
                    q.offer(new Node(nx, ny, now.island));
                    owner[nx][ny] = now.island;
                }

                // 누가 이미 방문 했을땐
                else {
                    result = Math.min(dist[now.x][now.y] + dist[nx][ny], result);
                }
            }
        }

        return result;
    }


    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};

    static void bfs(int x, int y) {

        Queue<Node> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][n];

        q.offer(new Node(x, y, cnt));
        visited[x][y] = true;
        map[x][y] = cnt;

        while (!q.isEmpty()) {
            Node now = q.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (!inRange(nx, ny)) continue;
                
                if (visited[nx][ny] || map[nx][ny] == 0) continue;

                visited[nx][ny] = true;
                q.offer(new Node(nx, ny, cnt));
                map[nx][ny] = cnt;
            }
        }

        cnt++;
    }

    static boolean inRange(int x, int y) {
        return (0<= x && x < n) && (0 <= y && y < n);
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}

class Node {
    int x, y, island;

    public Node(int x, int y, int island) {
        this.x = x;
        this.y = y;
        this.island = island;
    }
}
