import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Solution {

    static final StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static final StringBuilder sb = new StringBuilder();

    static final int PLUS = 0, MINUS = 1, MULTIPLY = 2, DIVISION = 3, OPERATOR_COUNT = 4;

    static int n;
    static int maxResult, minResult;
    static int[] numbers;
    static int[] operatorCnt;

    public static void main(String[] args) throws IOException {
        int tc = nextInt();

        for (int t = 1; t <= tc; t++) {
            n = nextInt();

            numbers = new int[n];
            operatorCnt = new int[OPERATOR_COUNT];

            maxResult = Integer.MIN_VALUE;
            minResult = Integer.MAX_VALUE;

            for (int i = 0; i < OPERATOR_COUNT; i++) {
                operatorCnt[i] = nextInt();
            }

            for (int i = 0; i < n; i++) {
                numbers[i] = nextInt();
            }
            
            permute(0, numbers[0]);

            sb.append("#").append(t).append(" ")
              .append(maxResult - minResult).append("\n");
        }

        System.out.print(sb);
    }

    // 순열
    static void permute(int depth, int curResult) {
        if (depth == n - 1) {
            maxResult = Math.max(maxResult, curResult);
            minResult = Math.min(minResult, curResult);
            return;
        }

        for (int i = 0; i < OPERATOR_COUNT; i++) {
            if (operatorCnt[i] == 0) continue;  // 남은 연산자가 없다면

            operatorCnt[i]--;
            int next = calc(curResult, numbers[depth + 1], i);
            permute(depth + 1, next);

            operatorCnt[i]++;   // 원복
        }
    }

    static int calc(int a, int b, int op) {
        switch (op) {
            case PLUS:     return a + b;
            case MINUS:    return a - b;
            case MULTIPLY: return a * b;
            case DIVISION: return a / b;
        }
        return 0;
    }

    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
}
