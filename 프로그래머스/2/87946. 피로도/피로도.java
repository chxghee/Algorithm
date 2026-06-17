import java.lang.Math;

class Solution {
    
    int result = 0, k, maxDungeonCnt;
    int[][] dungeons;
    boolean[] isSelected;
    
    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        this.maxDungeonCnt = dungeons.length;
        this.isSelected = new boolean[maxDungeonCnt];
        
        permute(0, k);
        
        return result;
    }
    
    void permute(int cnt, int curHp) {
        
        result = Math.max(result, cnt);
        
        for (int i = 0; i< maxDungeonCnt; i++) {
            if (isSelected[i]) continue;
            
            int needHp = dungeons[i][0];
            int consumeHp = dungeons[i][1];
            
            if (needHp > curHp) continue;
            
            isSelected[i] = true;
            permute(cnt + 1, curHp - consumeHp);
            isSelected[i] = false;
        }
    }
}