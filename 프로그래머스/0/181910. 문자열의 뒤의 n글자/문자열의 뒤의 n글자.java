class Solution {
    public String solution(String my_string, int n) {
       String answer = my_string;

       String result = answer.substring(answer.length()-n, answer.length());
        
       return result;
    }
}