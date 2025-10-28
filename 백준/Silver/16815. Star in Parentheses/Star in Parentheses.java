import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayDeque<Character> stack = new ArrayDeque<>();
        String string = br.readLine();
        char[] charArray = string.toCharArray();
        int result = 0;
        int flag = 0;
        for (char c : charArray) {

            if (c == '*') {
                flag = 1;
            }

            if (c == '(') {
                if (flag == 0) {    // 별 나오기 이전이면 add
                    stack.addLast(c);
                }
            } else {
                
                if (stack.isEmpty()) {
                    if (flag == 1) {    // 비어있는데 별 다음 부분이면 탐색 종료
                        break;
                    }
                    continue;       
                }

                if (flag == 1) {    // 별 다음부분인데 짝이 되는 닫는 괄호가 있다면 카운트
                    result += 1;
                }
                stack.removeLast();
            }
        }

        System.out.println(result);

    }
}
