import java.util.*;

class Solution {
    
    int n, m;
    int[][] maps;   // -1 이면 방문한 노드
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,-1,0,1};
    
    
    public int solution(int[][] maps) {
        this.maps = maps;
        this.n = maps.length;
        this.m = maps[0].length;
        
        return bfs();
    }
    
    int bfs() {
        Queue<Node> q = new ArrayDeque<>();
        
        q.offer(new Node(0, 0, 1));
        maps[0][0] = -1;
        
        while(!q.isEmpty()) {
            Node now = q.poll();
            
            if (now.x == n-1 && now.y == m-1) return now.level;
            
            for (int i = 0; i< 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if (!inRange(nx, ny)) continue;
                
                if (maps[nx][ny] != 1) continue;
                
                q.offer(new Node(nx, ny, now.level + 1));
                maps[nx][ny] = -1;
            }
            
        }
        
        return -1;
    }
    
    boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
    
    
}

class Node {
    int x, y, level;
    
    public Node(int x, int y, int level) {
        this.x = x;
        this.y = y;
        this.level = level;
    }
}
