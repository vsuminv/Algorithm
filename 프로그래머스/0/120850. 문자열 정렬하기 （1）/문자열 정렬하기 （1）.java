import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        int[] answer = {};
         ArrayList<Integer> list = new ArrayList<>();

        for(int i =0; i < my_string.length(); i++){
            char ch = my_string.charAt(i);
            if (Character.isDigit(ch)) {
                int num =Character.getNumericValue(ch);
                list.add(num);
                System.out.println(list.toString());
                
            }
            
        }
        answer = list.stream()
                .mapToInt(Integer::intValue) 
                .toArray();
        Arrays.sort(answer);
        
        return answer;
    }
}