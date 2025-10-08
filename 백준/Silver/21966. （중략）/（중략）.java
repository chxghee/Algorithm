import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();


        if (n <= 25) {
            System.out.println(str);
            return;
        }

        String[] strings = str.split("\\.");
        if (findFirst11thCharPosition(strings) == findLast11thCharPosition(strings)) {
            print(str, 11,11, "...");
        } else {
            print(str, 9,10, "......");
        }
        
    }

    public static int findFirst11thCharPosition(String[] strings) {
        int count = 0;
        for (int i = 0; i < strings.length; i++) {
            String string = strings[i];

            if (string.length() <= 11 - count) {
                count += string.length();
            } else {
                return i; // 현재 인덱스 반환
            }
        }
        return -1;
    }

    public static int findLast11thCharPosition(String[] strings) {
        int count = 0;
        for (int i = strings.length - 1; i >= 0; i--) {
            String string = strings[i];

            if (string.length() <= 11 - count) {
                count += string.length();
            } else {
                return i; // 현재 인덱스 반환
            }
        }
        return -1;
    }

    public static void print(String str, int frontLength, int rearLength, String splitter) {
        String string = str.substring(0, frontLength) + splitter + str.substring(str.length() - rearLength, str.length());
        System.out.println(string);
    }

}
