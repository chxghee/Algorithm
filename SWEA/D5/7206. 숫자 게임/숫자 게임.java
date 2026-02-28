import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Solution {

    static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    static StringBuilder sb = new StringBuilder();

    static int maxCount;

    public static void main(String[] args) throws IOException {

        int tc = nextInt();

        for (int t = 1; t <= tc; t++) {

            int number = nextInt();
            maxCount = Integer.MIN_VALUE;

            game(number, 0);
            
            sb.append('#').append(t).append(' ').append(maxCount).append('\n');
        }

        System.out.println(sb);
    }

    static void game(int number, int count) {

        if (number < 10) {
            maxCount = Math.max(maxCount, count);
            return;
        }

        String num = String.valueOf(number);
        int len = num.length();
        int maxMask = (1 << (len-1));

        for (int cutMask = 1; cutMask < maxMask; cutMask++) {        // 자를 위치가 주어짐
            int newNumber = 1;
            int cur = num.charAt(0) - '0';


            for (int i = 0; i < len-1; i++) {   // 각 비트를 확인 하기 위한
                int d = num.charAt(i+1) - '0';
                

                if ((cutMask & (1 << i)) != 0) { // 해당 자리에 비트가 있다면
                    // 뒤에 자르고
                    newNumber *= cur;
                    cur = d;
                } else {
                    cur = cur * 10 + d;
                }
            }
            newNumber *= cur;

            game(newNumber, count + 1);
        }

    }



    static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }    
}
