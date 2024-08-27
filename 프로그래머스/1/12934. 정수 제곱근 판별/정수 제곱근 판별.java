class Solution {
    public long solution(long n) {
        long answer = 0;
    
        if ( Math.pow((long)Math.sqrt(n),2)  == n){
            answer = (((long)Math.sqrt(n))+1)*(((long)Math.sqrt(n))+1);
        }
        else{
            answer = -1;
        }
        return answer;
    }
}