
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    static int[] parents;
    static int n, m;
    
    public static void main(String[] args) throws IOException {

        n = nextInt();
        m = nextInt();

        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        
        boolean flag = false;
        int count = 0;
        int result = 0;

        for (int i = 0; i < m; i++) {
            int a = nextInt();
            int b = nextInt();
        
            if (!flag && !union(a, b)) {    // 실행이 필요할 때만 union
                result = ++count;
                flag = true;
            }
            count++;
        }

        System.out.println(result);
    }

    // union find 에서 이미 속한 녀석이 나오면 사이클이다.
    static int find(int node) {

        if (parents[node] == node) {
            return node;
        }

        return parents[node] = find(parents[node]);
    }

    static boolean union(int a, int b) {

        int aParent = find(a);
        int bParent = find(b);

        if (aParent == bParent) return false;

        parents[bParent] = aParent; // 집합 B는 A에 합류 (부모를 수정해 주어야 함)
        return true;
    }
    
    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
