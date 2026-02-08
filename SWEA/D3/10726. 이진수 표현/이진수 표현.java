
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
            int n = nextInt();
            int m = nextInt();

            sb.append("#").append(t).append(" ").append(solve(n, m)).append("\n");
        }
        System.out.println(sb.toString());
    }

    static String solve(int n, int m) {
        int mask = (1 << n) - 1;

        if ((m & mask) == mask) return "ON";
        return "OFF";
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
