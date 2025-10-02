import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        List<Table> tables = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String command = scanner.next();

            // order
            if (command.equals("order")) {
                int tableNumber = scanner.nextInt();
                int time = scanner.nextInt();
                order(tables, tableNumber, time);
                print(tables);
            }

            // sorting
            else if (command.equals("sort")) {
                sort(tables);
                print(tables);
            }

            // complete
            else {
                int completeTable = scanner.nextInt();
                complete(tables, completeTable);
                print(tables);
            }
        }


        // 스캐너 close
        scanner.close();
    }

    private static void order(List<Table> tables, int table, int time) {
        tables.add(new Table(table, time));
    }

    private static void sort(List<Table> tables) {
        tables.sort(
                Comparator.comparingInt(Table::getTime)
                        .thenComparingInt(Table::getTable)
        );
    }
    
    private static void complete(List<Table> tables, int tableNumber) {
        for (Table t : tables) {
            if (tableNumber == t.getTable()) {
                tables.remove(t);
                return;
            }
        }
     }

    private static void print(List<Table> tables) {
        if (tables.isEmpty()) {
            System.out.println("sleep");
            return;
        }
        String collect = tables.stream()
                .map(t -> String.valueOf(t.table))
                .collect(Collectors.joining(" "));
        System.out.println(collect);
    }
}

class Table {
    int table;
    int time;

    public Table(int table, int time) {
        this.table = table;
        this.time = time;
    }

    public int getTable() {
        return table;
    }

    public int getTime() {
        return time;
    }
}
