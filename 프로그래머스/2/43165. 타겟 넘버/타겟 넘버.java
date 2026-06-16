class Solution {
    
    int cnt = 0, len, target;
    int[] numbers;
    
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        len = numbers.length;
        combination(0, 0);
        
        return cnt;
    }
    
    void combination(int idx, int sum) {
        
        if (idx == len) {
            if (sum == target) cnt++;
            return;
        }
        
        combination(idx + 1, sum + numbers[idx]);
        combination(idx + 1, sum + numbers[idx] * (-1));
    }
    
   
}