
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Solution {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {

        int tc = nextInt();
        
        for (int t = 1; t <= tc; t++) {
            sb.append("#").append(t).append(" ").append(solve(nextInt())).append("\n");
        }

        System.out.println(sb.toString());
    }

    static int solve(int n) {
        int visited = 0, i = 1, sheepCount, number, mod;
        int full = (1 << 10) - 1;   // 마스킹 설정

        while (true) {
            sheepCount = i * n;
            number = sheepCount;
            while (number > 0) {
                mod = number % 10;
                visited = visited | (full & (1 << mod));
                number /= 10;
            }

            if (visited == full) return sheepCount;

            i++;
        }
    }

    static boolean isAllVisited(boolean[] visited) {
        for (boolean v : visited) {
            if (!v) return false;
        }
        return true;
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    
}
