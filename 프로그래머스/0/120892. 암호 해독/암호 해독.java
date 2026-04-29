class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        String[] cipher_list = cipher.split("");
        for(int i =1; i < cipher_list.length+1; i++){
            if (i % code == 0){
                answer += cipher_list[i-1];
            }
        }
        return answer;
    }
}