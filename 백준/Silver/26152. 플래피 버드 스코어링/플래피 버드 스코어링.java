import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        int[] maxPassSize = new int[n];
        for (int i = 0; i < n; i++) {
            maxPassSize[i] = a[i] - b[i];
        }



        for (int i = 1; i < n; i++) {
            maxPassSize[i] = Math.min(maxPassSize[i], maxPassSize[i - 1]);
        }


        int q = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            System.out.println(binarySearch(maxPassSize, Integer.parseInt(st.nextToken())));
        }
    }


    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1, result = -1;


        while (left <= right) {

            int mid = (left + right) / 2;

            if (arr[mid] >= target) {
                result = mid;
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return result + 1;
    }
    
}
