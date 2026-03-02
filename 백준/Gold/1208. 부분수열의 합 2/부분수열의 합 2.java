
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.HashMap;
import java.util.Map;

public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }

    static int[] arr;
    static Map<Integer, Long> s1, s2;
    static boolean[] visited, isSelected;
    static int n, s;
    static long result = 0;

    public static void main(String[] args) throws IOException {
        
        s1 = new HashMap<>();
        s2 = new HashMap<>();

        n = nextInt();
        s = nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }

        int half = n / 2;
        subset(0, 0, half, s1);
        subset(half, 0, n, s2);

        solve();

        if (s == 0) result--;

        System.out.println(result);
    }

    static void solve() {
        
        for (int sum : s1.keySet()) {
            int target = s - sum;

            if (s2.containsKey(target)) {
                result += s2.get(target) * s1.get(sum);
            }
        }
    }

    static void subset(int index, int sum, int len, Map<Integer, Long> subsetSum) {

        if (index == len) {
            if (subsetSum.containsKey(sum)) {
                subsetSum.put(sum, subsetSum.get(sum) + 1L);
            } else {
                subsetSum.put(sum,1L);
            }
            return;
        }

        // 고른 경우
        subset(index + 1, sum + arr[index], len, subsetSum);

        // 안 고른 경우
        subset(index + 1, sum, len, subsetSum);
    }
}
