import java.util.*;
import java.io.*;

class Solution {
    
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Node> q = new ArrayDeque<>();
        int[] priorityRadix = new int[10];
        
        for (int i = 0; i < priorities.length; i++) {
            q.offer(new Node(i, priorities[i]));
            priorityRadix[priorities[i]]++;
        }
        
        while(true) {
            Node now = q.poll(); 
            
            int higher  = hasHigher(priorityRadix, now.priority);
            if (higher != now.priority) {   // 다시 넣고 반복
                q.offer(now);
                continue;
            } 
            
            if (now.num == location) {
                answer = priorities.length - q.size();
                break;
            }
            
            priorityRadix[now.priority]--;
        }
        
        return answer;
    }
    
    int hasHigher(int[] priorityRadix, int now) {
        for (int i = 9 ; i >= now; i--) {
            if (priorityRadix[i] != 0) {
                return i;
            }
        }
        return now;
    }
}

class Node {
    int num, priority;
    
    public Node (int num, int priority) {
        this.num = num;
        this.priority = priority;
    }
}