
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static Edge[] edges, mst;
    static int n, m, k;
    static int[] parents, elec;
    static boolean[] isElec;


    public static void main(String[] args) throws IOException {
        n = nextInt();
        m = nextInt();
        k = nextInt();

        isElec = new boolean[n+1];
        for (int i = 0; i < k; i++) {
            isElec[nextInt()] = true;
        }

        edges = new Edge[m];
        for (int i = 0; i < m; i++) {
            edges[i] = new Edge(nextInt(), nextInt(), nextInt());
        }

        
        System.out.println(kruskal());

    }

    // 부모를 만들때 발전소 노드면 발전소가 부모가 되어야 함
    // parents의 부모가 발전소 노드만 남을 때 까지 반복?
    static int kruskal() {
        Arrays.sort(edges);
        parents = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }

        int count = 0;
        int result = 0;

        for (Edge edge : edges) {
            
            if (!union(edge.start, edge.end)) continue;

            count++;
            result += edge.w;

            if (count == n-1-(k-1)) break;
            
        }

        return result;
    }

    static int find(int a) {

        if (parents[a] == a) {
            return a;
        }

        return parents[a] = find(parents[a]);
    }

    static boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);

        // aRoot, bRoot 둘다 발전소면 안됨 || 두 루트의 부모가 같으면 안됨
        if (isElec[aRoot] && isElec[bRoot]) return false;

        if (aRoot == bRoot) return false;

        // a가 루트라면
        if (isElec[aRoot]) {
            parents[bRoot] = aRoot;
        } else {
            parents[aRoot] = bRoot;
        } 
        return true;
    }


    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    
}

class Edge implements Comparable<Edge> {
    int start ,end, w;

    public Edge(int start, int end, int w) {
        this.start = start;
        this.end = end;
        this.w = w;
    }
    @Override
    public int compareTo(Edge o) {
        return Integer.compare(this.w, o.w);
    }
}
