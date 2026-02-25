import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static String str1, str2;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());

        for (int t = 1; t <= tc; t++) {
            st = new StringTokenizer(br.readLine());
            str1 = st.nextToken();
            str2 = st.nextToken();

            dp = new int[str1.length()+1][str2.length()+1];
            for (int[] row : dp) Arrays.fill(row, -1);

            int result = solve(0,0);

            sb.append('#').append(t).append(' ').append(result).append('\n');
        }
        System.out.println(sb);
    }

    static void bottomUpDp() {

        for (int i = 0; i < str1.length(); i++) {
            for (int j = 0; j < str2.length(); j++) {
                

                if (str1.charAt(i) == str2.charAt(j)) {
                }
                else {
                    dp[i+1][j+1] = Math.max(dp[i][j + 1], dp[i+1][j]);  // 같은 숫자가 없다면 나보다 이전 상황들에서 최대를 구한다.
                }
            }
        }
    }

    // top-down
    static int solve(int idx1, int idx2) {

        if (idx1 == str1.length() || idx2 == str2.length()) {
            return 0;
        }

        if (dp[idx1][idx2] != -1) return dp[idx1][idx2];

        if (str1.charAt(idx1) == str2.charAt(idx2)) {
            dp[idx1][idx2] = solve(idx1+1, idx2+1) + 1;
        }

        else {
            dp[idx1][idx2] = Math.max(solve(idx1+1, idx2), solve(idx1, idx2+1));
        }

        return dp[idx1][idx2];
    }
    
}
