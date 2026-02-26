
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static int k, w, h;
    static int[][] map;

    public static void main(String[] args) throws IOException {

        k = nextInt();
        w = nextInt();
        h = nextInt();

        map = new int[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                map[i][j] = nextInt();
            }
        }

        System.out.println(bfs());
    }

    static int[] dx = {0, 1, 0, -1, -2, -1, 1, 2, 2, 1, -1, -2};
    static int[] dy = {1, 0, -1, 0, 1, 2, 2, 1, -1, -2, -2, -1};

    static int bfs() {

        if (h == 1 && w == 1) return 0;

        Queue<Node> q = new ArrayDeque<>();
        int[][][] visited = new int[h][w][k+1];

        q.offer(new Node(0,0, 0));
        visited[0][0][0] = 1;

        while (!q.isEmpty()) {
            Node now = q.poll();
            int dc = now.kCnt == k ? 4 : 12;

            for (int i = 0; i < dc; i++) {

                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (!inRange(nx, ny)) continue;

                if (nx == h - 1 && ny == w - 1) {
                    return visited[now.x][now.y][now.kCnt];
                }
                
                int useK = i >= 4 ? 1 : 0;

                if (map[nx][ny] == 1 || visited[nx][ny][now.kCnt + useK] != 0) continue;

                q.offer(new Node(nx, ny, now.kCnt + useK));
                visited[nx][ny][now.kCnt + useK] = visited[now.x][now.y][now.kCnt] + 1;
            }
        }

        return -1;
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < h) && (0 <= y && y < w);
    }


    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    
}

class Node {

    int x, y, kCnt;

    public Node(int x, int y, int kCnt) {
        this.x = x;
        this.y = y;
        this.kCnt = kCnt;
    }
}
