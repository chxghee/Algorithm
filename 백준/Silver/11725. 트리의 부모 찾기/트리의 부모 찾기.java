
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;

    static int[] parentMemo;
    static int n;
    static List<List<Integer>> graph;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        graph = new ArrayList<>();


        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int u = Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        parentMemo = new int[n+1];
        

        bfs(1);
        for (int i = 2; i <= n; i++) {
            sb.append(parentMemo[i] + "\n");
        }
        System.out.println(sb);
    }


    public static void bfs(int start) {

        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new ArrayDeque<>();
        
        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (Integer adj : graph.get(now)) {
                if (visited[adj]) continue;
                
                parentMemo[adj] = now;
                queue.offer(adj);
                visited[adj] = true;
            }
        }
    }
}
