
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedReader br = new BufferedReader(new StringReader(INPUT));
        StringBuilder sb = new StringBuilder();

        int testCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCount; i++) {
            KeyLogger kl = new KeyLogger();
            
            String input = br.readLine();
            for (int j = 0; j < input.length(); j++) {
                char key = input.charAt(j);

                switch (key) {
                    case '<':
                        kl.left();
                        break;
                    case '>':
                        kl.right();
                        break;
                    case '-':
                        kl.remove();
                        break;
                
                    default:    // 문자일 때
                        kl.keyPressed(key);
                        break;
                }
            }

            sb.append(kl.getKeyLog())
                .append("\n");
        }

        System.out.println(sb);
    }

    static String INPUT = "2\r\n" + //
                "<<BP<A>>Cd-\r\n" + //
                "ThIsIsS3Cr3t";

}

class KeyLogger {

    Deque<Character> stack = new ArrayDeque<>();
    Deque<Character> subStack = new ArrayDeque<>();
    String result = "";

    public void left() {

        if (stack.isEmpty()) return;

        char poped = stack.pop();
        subStack.push(poped);
    }

    public void right() {
        if (subStack.isEmpty()) return;

        char poped = subStack.pop();
        stack.push(poped);
    }

    public void remove() {
        if (stack.isEmpty()) return;

        stack.pop();
    }

    public void keyPressed(char key) {
        stack.push(key);
    }

    public String getKeyLog() {
        StringBuilder sb = new StringBuilder();
       
        while (!stack.isEmpty()) {
            sb.append(stack.removeLast());
        }

        while (!subStack.isEmpty()) {
            sb.append(subStack.pop());
        }

        return sb.toString();
    }

}
