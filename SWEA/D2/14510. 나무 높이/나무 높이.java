
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;


public class Solution {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    static int n, maxTree;
    static int[] trees;

    public static void main(String[] args) throws IOException {
        int tc=  nextInt();

        for (int t = 1; t <= tc; t++) {
            n = nextInt();
            maxTree = 0;

            trees = new int[n];
            for (int i = 0; i < n; i++) {
                trees[i] = nextInt();
                maxTree = Math.max(maxTree, trees[i]);
            }
            sb.append("#").append(t).append(' ').append(solve()).append("\n");
        }

        System.out.println(sb.toString());
    }
    
    
    
    static int solve() {    
        int one = 0;
        int two = 0;

        for (int i = 0; i < trees.length; i++) {
            int diff = maxTree - trees[i];
            
            if (diff % 2 != 0) one++;

            two += diff / 2;
        }

        while (two > one + 1) {
            two--;
            one += 2;
        }

        if (one > two) return one * 2 - 1;
        return two * 2;
       
    }


    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}


