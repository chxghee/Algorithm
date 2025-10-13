import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] pointers = new int[m];

        for (int i = 0; i < m; i++) {
            pointers[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "assign":
                    assign(pointers);
                    break;
                case "swap":
                    swap(pointers);
                    break;
                default:
                    reset(pointers);
            }
        }


        int count = 0;
        int[] radix = new int[n];
        for (int i = 0; i< m;i++) {
            if (pointers[i] != 0 && radix[pointers[i]-1] == 0) {
                radix[pointers[i]-1] = 1;
                count += 1;
            }
        }

        System.out.println(count);
        for (int i = 0; i < n; i++) {
            if (radix[i] != 0) {
                System.out.println(i+1);
            }
        }

    }


    public static void assign(int[] pointers) {
        int x = Integer.parseInt(st.nextToken()) - 1;
        int y = Integer.parseInt(st.nextToken()) - 1;
        pointers[x] = pointers[y];
    }

    public static void swap(int[] pointers) {
        int x = Integer.parseInt(st.nextToken()) - 1;
        int y = Integer.parseInt(st.nextToken()) - 1;
        int temp = pointers[x];
        pointers[x] = pointers[y];
        pointers[y] = temp;
    }

    public static void reset(int[] pointers) {
        int x = Integer.parseInt(st.nextToken()) - 1;
        pointers[x] = 0;
    }

}
