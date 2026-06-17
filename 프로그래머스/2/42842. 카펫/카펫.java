import java.lang.Math;

class Solution {
    
    // r + c = (Y*B - Y + 4) / 2
    
    
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int lenSum = brown / 2 + 2;
        
        for (int r = 3;r < lenSum; r++ ) {
            int c = lenSum - r;
            
            if (r * c == brown+yellow) {
                answer[0] = Math.max(r,c);
                answer[1] = Math.min(r,c);
                return answer;
            }
        }
        
        
        return answer;
    }
    
    
}