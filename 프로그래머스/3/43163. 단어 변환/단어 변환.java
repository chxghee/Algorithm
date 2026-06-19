// 비긴과 타겟의 다른 문자의 현황을 조사하고 -> 베이스 문자열에서 일치하지 않는 문자 중에 점진적으로 변환 가능한지 안됨 

// 완전 탐색은? -> 백트래킹 가능하겠다. 
import java.lang.Math;
import java.io.*;

class Solution {
    
    int result = Integer.MAX_VALUE, wordsCount;
    boolean[] isSelected;
    String[] words;
    String begin, target;
    
    
    public int solution(String begin, String target, String[] words) {
        this.words = words;
        this.begin = begin;
        this.target = target;
        this.wordsCount = words.length;
        this.isSelected = new boolean[wordsCount];
        
        
        // 워드에 타켓 단어가 없는경우 빠르게 처리
        boolean hasTarget = false;
        for (String word : words) {
            if (word.equals(target)) hasTarget = true;
        }
        if (!hasTarget) return 0;
        
        // 백트랙 시작
        backtrack(0, begin, 0);
        System.out.println(result);
        
        if (Integer.MAX_VALUE == result) return 0;
        
        return result;
    }
    
    void backtrack(int cnt, String curWord, int selectCount) {
        
        // 타겟이랑 같으면 
        if (curWord.equals(target)) {
            result = Math.min(selectCount, result);
            return;
        }
        
        if (cnt == wordsCount) { // basecase
            return;
        }
        
        for (int i = 0; i< wordsCount;i++) {
            if (isSelected[i]) continue;
            
            if (!diffOnlyOneLetter(curWord, words[i])) continue;
            
            isSelected[i] = true;
            backtrack(cnt+1, words[i], selectCount+1);
            isSelected[i] = false;
        }
        
        
    }
    
    boolean diffOnlyOneLetter(String str1, String str2) {
        int diffCount = 0;
        
        for (int i = 0; i< str1.length(); i++) {
            if (str1.charAt(i) != str2.charAt(i)) diffCount++;
            
        }
        
        return diffCount == 1;
    }
}