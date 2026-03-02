import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }

    static int[] arr;
    static List<Integer> s1, s2;
    static boolean[] visited, isSelected;
    static int n, s;
    static long result = 0;

    public static void main(String[] args) throws IOException {
        
        s1 = new ArrayList<>();
        s2 = new ArrayList<>();
        
        n = nextInt();
        s = nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }

        if (s == 0) result--;

        int half = n / 2;
        subset(0, 0, half, s1);
        subset(half, 0, n, s2);

        solve();

        System.out.println(result);
    }

    static void solve() {
        Collections.sort(s1);
        for (Integer sum2 : s2) {
            int target = s - sum2;

            int low = lowerBiSearch(target);
            int high = upperBiSearch(target);
            
            result += high - low + 1;
        }
    }

    static int lowerBiSearch(int target) {
        int left = 0;
        int right = s1.size();
        
        while (left < right) {
            int mid = (left + right) / 2;
            
            if (s1.get(mid) >= target) right = mid;
            else left = mid + 1;
        }

        return left;
    }

    static int upperBiSearch(int target) {
        int left = 0;
        int right = s1.size();
        
        while (left < right) {
            int mid = (left + right) / 2;
            
            if (s1.get(mid) > target) right = mid;
            else left = mid + 1;
        }

        return left - 1;
    }

    static void subset(int index, int sum, int len, List<Integer> subsetSum) {

        if (index == len) {
            subsetSum.add(sum);
            return;
        }

        // 고른 경우
        subset(index + 1, sum + arr[index], len, subsetSum);

        // 안 고른 경우
        subset(index + 1, sum, len, subsetSum);
    }
}
