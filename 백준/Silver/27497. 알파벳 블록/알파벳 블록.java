import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Deque<String> deque = new ArrayDeque<>();
        Deque<Integer> history = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            if (command == 1) {
                String input = st.nextToken();
                deque.addLast(input);
                history.addLast(1);
            } else if (command == 2) {
                String input = st.nextToken();
                deque.addFirst(input);
                history.addLast(2);
            } else {
                if (history.isEmpty()) {
                    continue;
                }
                
                int last = history.removeLast();
                if (last == 1) {
                    deque.removeLast();
                } else {
                    deque.removeFirst();
                }
            }
        }

        if (deque.isEmpty()) {
            System.out.println(0);
            return;
        }

        StringBuilder sb = new StringBuilder();
        while (!deque.isEmpty()) {
            sb.append(deque.removeFirst());
        }
        System.out.println(sb);
    }
}
