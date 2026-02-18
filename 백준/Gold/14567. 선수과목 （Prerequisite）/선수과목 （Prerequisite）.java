
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

// https://www.acmicpc.net/problem/14567
public class Main {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    static int[] result, indegree;
    static int n,m;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        m = nextInt();

        result = new int[n+1];
        indegree = new int[n+1];
    
        graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        
        for (int i = 0; i < m; i++) {
            int a = nextInt();
            int b = nextInt();

            graph[a].add(b);
            indegree[b]++;
        }

        topologySort();

        for (int i = 1; i < n+1; i++) {
            sb.append(result[i]).append(' ');
        }
        
        System.out.println(sb);
    }

    static void topologySort() {
        Queue<Integer> queue = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
                result[i] = 1;
            }
        }

        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (Integer adj : graph[now]) {
                indegree[adj]--;

                if (indegree[adj] == 0) {
                    queue.offer(adj);
                    result[adj] = Math.max(result[adj], result[now] + 1);
                }
            }
        }
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    
}
