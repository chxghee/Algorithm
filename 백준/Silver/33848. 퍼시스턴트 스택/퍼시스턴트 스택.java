import java.util.*;

// https://www.acmicpc.net/problem/33848

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        PersistenceStack persistenceStack = new PersistenceStack();

        for (int i = 0; i < n; i++) {
            int command = scanner.nextInt();

            if (command == 1) { // push
                int number = scanner.nextInt();
                persistenceStack.push(number);
            } else if (command == 2) {  //pop
                persistenceStack.pop();
            } else if (command == 3) {  // cancel
                int j = scanner.nextInt();
                persistenceStack.cancel(j);
            } else if (command == 4) { // size
                System.out.println(persistenceStack.getSize());
            } else {    // top
                System.out.println(persistenceStack.getTop());
            }
        }

    }
}

class PersistenceStack {
    Stack<Integer> numbers = new Stack<>();
    Stack<Command> commands = new Stack<>();

    public void push(int number) {
        numbers.push(number);
        commands.push(new Command(1, number));
    }

    public void pop() {
        Integer popped = numbers.pop();
        commands.push(new Command(2, popped));
    }

    public void cancel(int j) {

        for (int i = 0; i < j; i++) {
            Command command = commands.pop();
            if (command.command == 1) {
                numbers.pop();
            } else {
                numbers.push(command.number);
            }
        }

    }

    public int getSize() {
        return numbers.size();
    }

    public int getTop() {
        if (numbers.isEmpty()) {
            return -1;
        }
        return numbers.peek();
    }

}

class Command {
    int command;
    int number;
    public Command(int command, int number) {
        this.command = command;
        this.number = number;
    }

}
