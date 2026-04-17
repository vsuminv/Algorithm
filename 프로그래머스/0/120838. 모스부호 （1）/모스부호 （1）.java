import java.util.HashMap;
import java.util.Map;
class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] letter_arr = letter.split(" ");
        
        String[] morse ={
                    ".-","-...","-.-.","-..",".","..-.",
                    "--.","....","..",".---","-.-",".-..",
                    "--","-.","---",".--.","--.-",".-.",
                    "...","-","..-","...-",".--","-..-",
                    "-.--","--.."};
        
        for(int i=0; i < letter_arr.length; i++){
            for(int j = 0; j < morse.length; j++){
                if (letter_arr[i].equals(morse[j])){
                    answer += (char)(j + 97);
                }
            }
        }

        return answer;
    }
}