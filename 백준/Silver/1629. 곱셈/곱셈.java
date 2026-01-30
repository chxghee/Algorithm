import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());

        System.out.println(power(a, b, c));
    }

    public static long power(long a, long n, long mod) {
        if (n == 1) {
            return a % mod;
        }

        long half = power(a, n / 2, mod);
        long result = half * half % mod;
        if (n % 2 != 0) {
            return result * a % mod;
        }
        return  result;
    }
}
