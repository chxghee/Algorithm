import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Set<String> participants = new HashSet<>();
        int count = 0;

        for (int i = 0; i < n; i++) {
            String str = br.readLine();

            if (str.equals("ENTER")) {
                participants.clear();
                continue;
            }
            if (participants.add(str)) {
                count++;
            }
        }

        System.out.println(count);
    }

}
