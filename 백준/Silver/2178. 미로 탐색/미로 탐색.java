import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int n,m;
    private static int[][] map;
    private static int[] dx = {0,1,0,-1};
    private static int[] dy = {1,0,-1,0};

    static int bfs() {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0});
        map[0][0] = 2;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];
            int depth = map[x][y];

            if (x == n-1 && y == m-1) {
                return depth - 1;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (check(nx, ny) && map[nx][ny] == 1) {
                    queue.offer(new int[]{nx, ny});
                    map[nx][ny] = depth + 1;
                }
            }
        }

        return -1;
    }

    static boolean check(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }

}
