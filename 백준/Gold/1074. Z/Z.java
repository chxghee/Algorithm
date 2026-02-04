
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    static int N, r, c;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int blockSize = (1 << (N));

        System.out.println(curr(r, c, blockSize));
    }


    static int curr(int curX, int curY, int blockSize) {
        if (blockSize <= 2) {
            if (curX ==0 && curY ==0) return 0;
            if (curX == 0 && curY == 1) return 1;
            if (curX == 1 && curY == 0) return 2;
            if (curX == 1 && curY == 1) return 3;
        }

        int half = blockSize >> 1;
        int position = findPosition(curX, curY, half);
        
        if (position == 0) {
            return position * half * half + curr(curX, curY, half);
        } else if (position == 1) {
            return position * half * half + curr(curX, curY - half, half);
        } else if (position == 2) {
            return position * half * half + curr(curX - half, curY, half);
        } else {
            return position * half * half + curr(curX  - half, curY - half, half);
        }
    } 

    static int findPosition(int x, int y, int half) {
        if (x < half && y < half) return 0;
        if (x < half && y >= half) return 1;
        if (x >= half && y < half) return 2;
        if (x >= half && y >= half) return 3;

        return -1;
    }
}
