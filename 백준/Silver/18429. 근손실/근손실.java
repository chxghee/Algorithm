
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    
    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static int n, k, count = 0;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        k = nextInt();
        arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }

        permutation(0);
        System.out.println(count);
    }

    static void permutation(int fixedIdx) {
        if (fixedIdx == arr.length) {
            count += isPossible(arr);
            return;
        }

        for (int i = fixedIdx; i < arr.length; i++) {
            swap(fixedIdx, i);
            permutation(fixedIdx + 1);
            swap(fixedIdx, i);
        }
    }



    static void swap(int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }


    static int isPossible(int[] arr) {
        int loss = 0;

        for (int e : arr) {

            loss += e - k;
            if (loss < 0) {
                return 0;
            }
        }

        return 1;
    }
    
    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
