import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

//        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        List<List<Integer>> graph = new ArrayList<>();
        settingGraph(n, graph, m, br);

        boolean[] visited = new boolean[n+1];  // 전부 false
        int result = 0;
        Deque<Integer> queue = new ArrayDeque<>();


        for (int i = 1; i < n + 1; i++) {
            if (!visited[i]) {
                visited[i] = true;
                queue.add(i);

                while (!queue.isEmpty()) {
                    int now = queue.removeFirst();

                    for (Integer adj : graph.get(now)) {
                        if (!visited[adj]) {
                            queue.add(adj);
                            visited[adj] = true;
                        }
                    }

                }
                result += 1;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }

    private static void settingGraph(int n, List<List<Integer>> graph, int m, BufferedReader br) throws IOException {
        StringTokenizer st;
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
    }
}
