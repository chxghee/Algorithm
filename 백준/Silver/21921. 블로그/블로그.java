
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        int accSum = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (i < x) accSum += arr[i];
        }

        int max = accSum;
        int count = 1;

        for (int i = 0; i < n - x; i++) {
            accSum = accSum + arr[x+i] - arr[i];

            if (accSum < max) continue;

            if (accSum == max) count++;
            if (accSum > max) count = 1;
            max = accSum;
        }        
        
        if (max == 0) {
            System.out.println("SAD");
            return;
        }

        System.out.println(max + "\n" + count);
    }
    
}
