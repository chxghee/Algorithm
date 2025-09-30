import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int s = scanner.nextInt();
        int n = scanner.nextInt();      // 저장
        int m = scanner.nextInt();      // 삭제

        DynamicArray dynamicArray = new DynamicArray(s);

        for (int i = 0; i < n + m; i++) {
            int input = scanner.nextInt();

            if (input == 1) {
                dynamicArray.append();
            } else {
                dynamicArray.delete();
            }
        }

        System.out.println(dynamicArray.getMaxSize());
    }

}

class DynamicArray {

    private int maxSize;
    private int currentSize;

    public DynamicArray(int maxSize) {
        this.maxSize = maxSize;
        this.currentSize = 0;
    }

    public void append() {
        if (maxSize == currentSize) {
            maxSize *= 2;
        }
        this.currentSize++;
    }

    public void delete() {
        currentSize--;
    }

    public int getMaxSize() {
        return maxSize;
    }
}
