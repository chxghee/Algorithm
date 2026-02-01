
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());


        BigInteger result = hanoi1(n);
        if (n > 20) {
            System.out.println(result);
            return;
        }

        hanoi2(n,1,3,2);
        
        System.out.println(result);
        System.out.println(sb.toString());
    }

    
    public static BigInteger hanoi1(int n) {
        if (n == 1) {
            return BigInteger.valueOf(1);
        }
        return hanoi1(n - 1).multiply(BigInteger.valueOf(2)).add(BigInteger.ONE);
    }

    public static void hanoi2(int n, int start, int end, int sub) {
        
        if (n == 1) {
            sb.append(start).append(" ").append(end).append("\n");
            return;
        }
        
        hanoi2(n - 1, start, sub, end);
        sb.append(start).append(" ").append(end).append("\n");
        hanoi2(n - 1, sub, end, start);
    }
}