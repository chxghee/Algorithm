import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }

    static int[] arr, a, b;
    static boolean[] visited, isSelected;
    static int n, s, result = 0;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        s = nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }

        if (s == 0) result--;

        subset(0, 0);

        System.out.println(result);

    }


    static void subset(int index, int sum) {


        if (index == n) {
            if (sum == s) result++; 
            return;
        }


        // 고른 경우
        subset(index + 1, sum + arr[index]);

        // 안 고른 경우
        subset(index + 1, sum);
    }

}
