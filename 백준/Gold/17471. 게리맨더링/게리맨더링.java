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
    static StringBuilder sb = new StringBuilder();
    static int[] popul;
    static boolean[] isSelected;
    static int n, result = Integer.MAX_VALUE, total = 0;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        isSelected = new boolean[n+1];

        popul = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            popul[i] = nextInt();
            total += popul[i];
        }
    
        graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n; i++) {
            int adjCount = nextInt();
            for (int j = 0; j < adjCount; j++) {
                int v = nextInt();
                graph[i].add(v);
            }
        }

        // logic
        subset(1, 0);

        if (result == Integer.MAX_VALUE) {
            System.out.println(-1);
            return;
        }

        System.out.println(result);
    }

    static void subset(int number, int selectCnt) {

        if (number > n) {  // 부분 집합 완성
            if (selectCnt > 0 && selectCnt < n) check(selectCnt); 
            return;
        }

        isSelected[number] = true;
        subset(number + 1, selectCnt + 1);

        isSelected[number] = false;
        subset(number + 1, selectCnt);
    }

    static void check(int selectCnt) {
        
        int start1 = -1, start2 = -1;

        for (int i = 1; i <= n; i++) {
            if (isSelected[i] && start1 == -1) start1 = i;
            if (!isSelected[i] && start2 == -1) start2 = i;
        }


        int r1 = bfs(selectCnt, start1, true);
        int r2 = bfs(n - selectCnt, start2, false);

        if (r1 != -1 && r2 != -1) {
            result = Math.min(result, Math.abs(r1-r2));
        }
    }

    static int bfs(int targetCnt, int start, boolean team) {
        
        int count = 0, sum = 0;
        boolean[] visited = new boolean[n+1];

        Queue<Integer> q = new ArrayDeque<>();

        q.offer(start);
        visited[start] = true;
        count++;
        sum = popul[start];

        while (!q.isEmpty()) {
            int now = q.poll();

            for (Integer adj : graph[now]) {
                
                if (visited[adj]) continue;

                if (isSelected[adj] == team) {
                    q.offer(adj);
                    visited[adj] = true;
                    count++;
                    sum += popul[adj];
                }
            }
        }

        if (count == targetCnt) return sum;
        return -1;
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    
}
