import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StreamTokenizer st = new StreamTokenizer(br);

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();

        int n = nextInt();
        int q = nextInt();

        boolean[] treeArray = new boolean[n+1];
        int land;
        for (int i = 0; i < q; i++) {
            land = nextInt();
            sb.append(canReach(treeArray, land)).append("\n");
        }
        System.out.println(sb.toString());
    }

    public static int canReach(boolean[] tree, int target) {
        int idx = target;
        int landNo = 0;

        while (idx > 0) {

            if (tree[idx]) {
                landNo = idx; 
            } 

            idx /= 2;
        }

        if (landNo == 0) tree[target] = true;

        return landNo;
    }

    public static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}