import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n;
    static int[][] image;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) throws IOException {
        
        int n = Integer.parseInt(br.readLine());

        image = new int[n][n];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();

            for (int j = 0; j < n; j++) {
                image[i][j] = input.charAt(j) - '0';
            }
        }

        quadTree(0, 0, n, 0);

        sb.deleteCharAt(0);
        System.out.println(sb.toString());
    }

    static void quadTree(int row, int col, int size, int order) {

        int blackCount = 0;
        for (int i = row; i < size + row; i++) {
            for (int j = col; j < size + col; j++) {
                blackCount += image[i][j];
            }
        }
        
        if (order == 0) {
            sb.append('(');
        }
        
        if (blackCount == size * size) {    // 블랙 칸일 때
            sb.append(1);
        } else if (blackCount == 0) {   // 화이트 칸일 때
            sb.append(0);
        } else {

            int half = size / 2;
            quadTree(row, col, half, 0);
            quadTree(row, col + half, half, 1);
            quadTree(row + half, col, half, 2);
            quadTree(row + half, col + half, half, 3);
        }

        if (order == 3) {
            sb.append(')');
        }
    }
}