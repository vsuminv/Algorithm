class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        String[] arr_string = my_string.split("");

        for (int i = 0; i < arr_string.length; i++){
            if (arr_string[i].equals(letter)){
                
                continue;
            }
            else{
                answer += arr_string[i];    
            }
            
        }
        
        return answer;
    }
}