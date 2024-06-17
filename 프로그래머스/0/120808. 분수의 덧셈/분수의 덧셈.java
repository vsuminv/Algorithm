class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        int top = (numer1 * denom2) + (numer2 * denom1);
        int bottom = denom1 * denom2;
        int t = top;
        int b = bottom;
        
        while( b != 0){
            b = t % b;
            t = b;
        }
        answer[0] = top/t;
        answer[1] = bottom/b;
        
        
            
        
        
        
            

        return answer;
    }
}