import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
          Integer[] scoreInteger = Arrays.stream(score).boxed().toArray(Integer[]::new);
        
        
        Arrays.sort(scoreInteger, Collections.reverseOrder());

       
        for (int i = 0; i <= scoreInteger.length - m; i += m) {
            int boxMin = scoreInteger[i + m - 1]; 
            answer += boxMin * m; 
        }
        return answer;
    }
}