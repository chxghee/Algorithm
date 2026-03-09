
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    static int[] arr, a, b;
    static boolean[] visited, isSelected;
    static int n, result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        arr = new int[n];
        visited = new boolean[n];
       

        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }

        System.out.println(calcResult());   
    }

    static int calcResult() {
        int cycleCnt = 0;
        for (int i = 0; i < n; i++) {

            if (visited[i]) continue;

            cycleCnt++;

            visited[i] = true;
            int now = i;
            while (true) {
                int next = arr[now];

                if (visited[next]) {
                    break;
                }

                visited[next] = true;
                now = next;
            }
        }

        return cycleCnt == 1 ? 0 : cycleCnt;
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
