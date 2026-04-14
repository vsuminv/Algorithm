class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String [] arr_string = my_string.split("");
        for(int i =0 ; i < arr_string.length; i++){
            answer += arr_string[i].repeat(n);
        }
        return answer;
    }
}