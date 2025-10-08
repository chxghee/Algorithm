import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int sample = scanner.nextInt();
        int system = scanner.nextInt();
        int sampleFlag = 0;
        int systemFlag = 0;

        for (int i = 0 ; i < sample ; i++) {
            long manAnswer = scanner.nextLong();
            long answer = scanner.nextLong();

            if (manAnswer != answer) {
                sampleFlag = 1;
                break;
            }
        }

        for (int i = 0 ; i < system ; i++) {
            long manAnswer = scanner.nextLong();
            long answer = scanner.nextLong();

            if (manAnswer != answer) {
                systemFlag = 1;
                break;
            }
        }

        if (sampleFlag == 0 && systemFlag == 0) {
            System.out.println("Accepted");
        }
        else if (sampleFlag == 1) {
            System.out.println("Wrong Answer");
        }
        else {
            System.out.println("Why Wrong!!!");
        }


        // 스캐너 close
        scanner.close();
    }

}
