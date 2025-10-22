import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        MyStack stack = new MyStack();
        ArrayList<String> results = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 가능하려면 현재 수열의 수 만큼 push 가 되어야 함
        // 그 다음 수는 크면 일단 그 다음은 무조건 가능하긴함
        // 그담수는 작다면 아직 안 뽑힌 수 중에 가장 큰 수여야
        int flag = 0;
        for (int number : arr) {
            if (number < stack.top()) {
                flag =1;
                break;
            } else if (number == stack.top()) {
                stack.pop();
                results.add("-");
            } else {
                // 만약 현재까지 pushed 최대 숫자 보다 큰 숫자가 나오면
                for (int i = stack.getMaxPushedNumber() + 1; i <= number; i++) {
                    stack.push(i);
                    results.add("+");
                }
                stack.pop();
                results.add("-");
            }
        }

        if (flag == 1) {
            System.out.println("NO");
        } else {
            for (String result : results) {
                System.out.println(result);
            }
        }

    }
}

class MyStack {

    Stack<Integer> stack = new Stack<>();
    int maxPushedNumber = 0;

    public void push(int x) {
        stack.push(x);
        maxPushedNumber = x;
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        if (stack.isEmpty()) {
            return 0;
        }
        return stack.peek();
    }

    public int getMaxPushedNumber() {
        return maxPushedNumber;
    }

    public void print() {
        stack.forEach(System.out::print);
    }
}
