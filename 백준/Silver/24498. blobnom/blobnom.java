import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        // 결국은 옆에 애들을 소모해서 올릴 수 있어야 하는 최대 높이
        // 현재 가장 높다고 좋은게 아님
        // 옆에 애들 두개 써서 1개을 올리는 것
        // -> 그렇기 때문에 저 멀리 있는 봉우리를 위해 옆 기반을 다지려 땅을 뺏오온다 해도 봉우리가 소모될 수 밖에 없어서 안됨
        int result = 0;
        for (int i = 0; i < n; i++) {

            if (i == 0 || i == n-1) {
                result = Math.max(result, a[i]);

            } else {
                result = Math.max(result, a[i] + maxStackableBlob(a[i-1], a[i+1]));
            }
        }


        System.out.println(result);

    }

    // 올릴 수 있는 최대 블롭 개수
    public static int maxStackableBlob(int x, int y) {
        return Math.min(x,y);
    }

}
