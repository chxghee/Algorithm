import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[][] home;
    static int flag = 2;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static boolean check(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    public static int bfs(int x, int y){

        Deque<int[]> queue = new ArrayDeque<>();

        queue.offer(new int[]{x, y});
        home[x][y] = flag;  // 방문처리
        int count = 1;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (check(nx,ny) && home[nx][ny] == 1) {
                    queue.offer(new int[]{nx, ny});
                    home[nx][ny] = flag; // 방문처리
                    count += 1;
                }
            }
        }

        flag += 1;
        return count;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        // 입력
        home = new int[n][n];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                home[i][j] = input.charAt(j) - '0';
            }
        }


        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (home[i][j] == 1) {
                    results.add(bfs(i, j));
                }
            }
        }

        Collections.sort(results);

        StringBuilder sb = new StringBuilder();
        sb.append(results.size()).append("\n");
        for (Integer result : results) {
            sb.append(result)
                    .append("\n");
        }

        System.out.println(sb.toString());
    }
}
