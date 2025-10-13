import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()) - 1;
        int m = Integer.parseInt(br.readLine()) - 1;
        if (n < 1 || m < 1) {
            System.out.println(0);
            return;
        }
        System.out.println(n*m*2);
    }

}
