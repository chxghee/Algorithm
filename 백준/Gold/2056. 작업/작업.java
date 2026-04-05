
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
    static int[] works, indgree, parent;
    static int n;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {

        n = nextInt();

        indgree = new int[n+1];
        graph = new ArrayList[n+1];
        works = new int[n+1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 1; i <= n; i++) {
            int t = nextInt();
            works[i] = t;
            int m = nextInt();
            for (int j = 0; j < m; j++) {
                int first = nextInt();
                graph[first].add(i);
            }
            indgree[i] = m;
        }

        System.out.println(topology());
    }

    static int topology() {
    
        // 각 작업이 끝나는 시간들을 기록해서 가장 오래 걸리는 루트가 답이 되는 것임
        int[] endTime = new int[n+1];

        // 진입 차수 0인거 저장
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            if (indgree[i] == 0) {
                q.offer(i);
                endTime[i] = works[i];
            } 
        }
        
        while (!q.isEmpty()) {
            int now = q.poll();
    
            for (Integer adj : graph[now]) {

                endTime[adj] = Math.max(endTime[adj], endTime[now] + works[adj]);
                indgree[adj]--;
                if (indgree[adj] == 0) q.offer(adj);
            }
        }

        int time = 0;
        for (int i = 1; i <= n; i++) {
            time = Math.max(time, endTime[i]);
        }

        return time;
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
