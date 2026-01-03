import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int n;
    private static char[][] map1;
    private static char[][] map2;
    private static int[] dx = {0,1,0,-1};
    private static int[] dy = {1,0,-1,0};

    private static int aggregate(char[][] map, boolean isNormal) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] != '0') {
                    bfs(i, j, map, isNormal);
                    result += 1;
                }
            }
        }
        return result;
    }


    private static void bfs(int i, int j, char[][] map,  boolean isNormal) {

        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{i, j});
        char baseColor = map[i][j];
        map[i][j] = '0';

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (check(nx,ny) && isSameColor(baseColor, map[nx][ny], isNormal)) {
                    queue.offer(new int[]{nx, ny});
                    map[nx][ny] = '0';
                }
            }
        }
    }

    static boolean isSameColor(char baseColor, char newColor, boolean isNormal) {
        if (isNormal) {
            return baseColor == newColor;
        }

        if (baseColor == 'B') {
            return newColor == 'B';
        }

        return newColor == 'R' || newColor == 'G';
    }

    static boolean check(int x, int y) {
        return 0<=x && x<n && 0<=y && y<n;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map1 = new char[n][n];
        map2 = new char[n][n];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                map1[i][j] = input.charAt(j);
                map2[i][j] = input.charAt(j);
            }
        }

        int normal = aggregate(map1, true);
        int disorder = aggregate(map2, false);
        System.out.println(normal + " " + disorder);
    }

}
