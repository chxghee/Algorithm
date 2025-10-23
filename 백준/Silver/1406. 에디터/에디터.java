import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1406

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        String str = br.readLine();

        Editor editor = new Editor(str);
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "L":
                    editor.moveLeft();
                    break;
                case "D":
                    editor.moveRight();
                    break;
                case "B":
                    editor.delete();
                    break;
                default:
                    editor.insert(st.nextToken().charAt(0));
                    break;
            }
        }

        editor.print();
    }
}

class Editor {

    Stack<Character> left = new Stack<>();
    Stack<Character> right = new Stack<>();

    public Editor(String str) {
        for (char c : str.toCharArray()) {
            left.push(c);
        }
    }

    public void moveLeft() {
        if (left.isEmpty()) {
            return;
        }
        right.push(left.pop());
    }

    public void moveRight() {
        if (right.isEmpty()) {
            return;
        }
        left.push(right.pop());
    }

    public void insert(Character character) {
        left.push(character);
    }

    public void delete() {
        if (left.isEmpty()) {
            return;
        }
        left.pop();
    }

    public void print() {

        StringBuilder sb = new StringBuilder();

        for (Character c : left) {
            sb.append(c);
        }
        while (!right.isEmpty()) {
            sb.append(right.pop());
        }
        System.out.println(sb);
    }

}
