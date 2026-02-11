import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Scanner;

public class Solution {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();
    static Scanner sc = new Scanner(System.in);

    static int n;
    static int[] h; 

    public static void main(String[] args) throws IOException {

        int tc = nextInt();

        for (int t = 1; t <= tc; t++) {
            n = nextInt();
            
            h = new int[n];
            for (int i = 0; i < n; i++) {
                h[i] = nextInt();
            }

            sb.append("#").append(t).append(' ').append(solve()).append("\n");
        }

        System.out.println(sb);
    }

    static int solve() {
        int count = 0, upCnt = 0, downCnt = 0, now = 0;

        while (now < n - 1) {

            while (now < n - 1 && h[now] < h[now + 1]) {
                upCnt++;
                now++;
            }
            while (now < n - 1 && h[now] > h[now + 1]) {
                downCnt++;
                now++;
            }

            if (upCnt == 0 && downCnt == 0) now++;

            // 여기까지 내려왔다는 것은 산 만들가 끝났다는것
            count += upCnt * downCnt;
            upCnt = 0;
            downCnt = 0;
        }

        return count;
    }

    
    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}

