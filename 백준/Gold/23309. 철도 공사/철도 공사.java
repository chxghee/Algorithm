import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int first = Integer.parseInt(st.nextToken());
        NodeArray nodeArray = new NodeArray(first);
        int prev = first;

        for (int i = 1; i < n; i++) {
            int newNode = Integer.parseInt(st.nextToken());
            nodeArray.addLast(prev, newNode);
            prev = newNode;
        }
        

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            
            st = new StringTokenizer(br.readLine());

            String command = st.nextToken();
            int at, id, result;
            
            switch (command) {
                case "BN":  // 다음에 추가
                    at = Integer.parseInt(st.nextToken());
                    id = Integer.parseInt(st.nextToken());

                    result = nodeArray.addNext(at, id);
                    sb.append(result + "\n");
                    break;
                case "BP":
                    at = Integer.parseInt(st.nextToken());
                    id = Integer.parseInt(st.nextToken());

                    result = nodeArray.addPrev(at, id);
                    sb.append(result + "\n");
                    break;
                case "CP":  // 이전 삭제 
                    at = Integer.parseInt(st.nextToken());

                    result = nodeArray.removePrev(at);
                    sb.append(result + "\n");
                    break;
                case "CN":  // 현재 삭제
                    at = Integer.parseInt(st.nextToken());

                    result = nodeArray.removeNext(at);
                    sb.append(result + "\n");
                    break;
            
                default:
                    break;
            }
        }
        
        System.out.println(sb);
        
    }
}

class NodeArray {
    
    int first;
    int[] prev = new int[1_000_001];
    int[] next = new int[1_000_001];

    public NodeArray(int first) {
        prev[first] = first;
        next[first] = first;
        this.first = first;
    }

    public void addLast(int nowNode, int newNode) {
        next[nowNode] = newNode;
        prev[newNode] = nowNode;
        prev[first] = newNode;
        next[newNode] = first;
    }

    public int addNext(int at, int newNode) {

        int nextNode = next[at];
        prev[nextNode] = newNode;

        next[at] = newNode;

        prev[newNode] = at;
        next[newNode] = nextNode;
        
        return nextNode;        // 다음 정거장 번호 리턴
    }

    public int addPrev(int at, int newNode) {
        
        int prevNode = prev[at];
        next[prevNode] = newNode;

        prev[at] = newNode;

        prev[newNode] = prevNode;
        next[newNode] = at;
        
        return prevNode;        // 다음 정거장 번호 리턴
    }

    public int removeNext(int at) {

        int deletedNode = next[at];
        int nextNode = next[deletedNode];

        next[at] = nextNode;
        prev[nextNode] = at;

        next[deletedNode] = 0;
        prev[deletedNode] = 0;

        return deletedNode;
    }

    public int removePrev(int at) {

        int deletedNode = prev[at];
        int prevNode = prev[deletedNode];

        prev[at] = prevNode;
        next[prevNode] = at;

        next[deletedNode] = 0;
        prev[deletedNode] = 0;

        return deletedNode;
    }
}
