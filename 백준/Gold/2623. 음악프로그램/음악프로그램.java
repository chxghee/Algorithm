
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;


public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static int n, m;
    static int[] indegree, order;
    static StringBuilder sb = new StringBuilder();
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        m = nextInt();

        indegree = new int[n+1];
        graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int k = nextInt();

            order = new int[k];
            for (int j = 0; j < k; j++) {
                order[j] = nextInt();
            }

            for (int j = 0; j < k-1; j++) {
                int from = order[j];
                int to = order[j+1];

                graph[from].add(to);
                indegree[to]++;
            }

        }

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 1; i < n+1; i++) {
            if (indegree[i]==0)
                q.offer(i);
        }

        int count = 0;

        while (!q.isEmpty()) {
            int now = q.poll();
            sb.append(now).append('\n');
            count++;

            for (int adj : graph[now]) {
                indegree[adj]--;
                if(indegree[adj] == 0) {
                    q.offer(adj);
                }
            }
        }

        if (count !=n) {
            System.out.println(0);
            return;
        }

        System.out.println(sb.toString());

    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
