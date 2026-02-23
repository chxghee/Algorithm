import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
        
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuffer sb;

    static int[] arr;
    static int answer = Integer.MIN_VALUE;
    static int n,k;

    public static void main(String[] args) throws IOException {
        
        st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        arr = new int[k];
        for (int i = 0; i < k; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        dfs(0);

        System.out.println(answer);
    }

    public static void dfs(int curNumber) {

        if (curNumber > n) return;

        answer  = Math.max(answer, curNumber);

        for (int i = k-1; i >= 0; i--) {
            dfs(curNumber * 10 + arr[i]);
        }

    }


    static String TEST_CASE = "110 3\r\n" + //
                "1 5 7";
}
