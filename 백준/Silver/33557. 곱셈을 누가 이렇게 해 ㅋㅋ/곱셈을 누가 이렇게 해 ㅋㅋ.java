import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            long a = scanner.nextLong();
            long b = scanner.nextLong();
            long result = wrongMultiplication(a, b);

            if (result == a*b) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }

    }

    public static long wrongMultiplication(long a, long b) {

        String[] arrayA = String.valueOf(a).split("");
        String[] arrayB = String.valueOf(b).split("");
        List<Integer> results = new ArrayList<>();

        int i = arrayA.length - 1;
        int j = arrayB.length - 1;

        for (; i >= 0 || j >= 0; i--, j--) {

            int na = 1;
            int nb = 1;
            if (i >= 0) {
                na = na * Integer.parseInt(arrayA[i]);
            }

            if (j >= 0) {
                nb = nb * Integer.parseInt(arrayB[j]);
            }

            results.add(na*nb);
        }

        String result = "";
        for (Integer integer : results) {
            String s = String.valueOf(integer);
            result = s + result;
        }

        return Long.parseLong(result);
    }

}
