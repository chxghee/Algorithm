import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.nextLine(); // 버퍼 비우기

        String st = scanner.nextLine();
        Set<Integer> set1 = Arrays.stream(st.split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toSet());
        st = scanner.nextLine();
        Set<Integer> set2 = Arrays.stream(st.split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toSet());

        TreeSet<Integer> result = new TreeSet<>();

        for (Integer num : set1) {
            if (!set2.contains(num)) {
                result.add(num);
            }
        }

        if (result.isEmpty()) {
            System.out.println(0);
            return;
        }


        System.out.println(result.size());
        StringBuilder sb = new StringBuilder();
        for (Integer i : result) {
            sb.append(i).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
