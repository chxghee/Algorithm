import java.util.*;


class Solution {
    
    List<Integer>[] graph;
    int result;
    
    public int solution(int n, int[][] edge) {
        graph = new ArrayList[n+1];
        for (int i=1;i<n+1;i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i =0; i< edge.length;i++) {
            int u = edge[i][0], v = edge[i][1];
            graph[u].add(v);
            graph[v].add(u);
        }
        
        
        
        
        return bfs(n);
    }
    
    
    int bfs(int nodeSize) {
        
        int[] dist = new int[nodeSize + 1];
        boolean[] visited = new boolean[nodeSize+1];
        Queue<Integer> q = new ArrayDeque<>();
        
        q.offer(1);
        visited[1] = true;
        dist[1] = 1;
        int maxDist = 0;
        
        while (!q.isEmpty()) {
            int now = q.poll();
            
            for (int adj : graph[now]) {
                
                if (visited[adj]) continue;
                
                visited[adj] = true;
                dist[adj] = dist[now] + 1;
                maxDist = dist[adj];
                q.offer(adj);
            }
        }
        int result = 0; 
        for (int i = 0; i< nodeSize + 1; i++) {
            if (dist[i] == maxDist) result++;
        }
        return result;
    }
    
}

class Node {
    
}