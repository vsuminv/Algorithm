import java.util.*;
class Solution {
    public String solution(int[] food) {
        String answer = "";
        int cal = 0;
        String a = "";
        List<String> food_list = new ArrayList<String>();
        StringBuilder f = new StringBuilder();
        StringBuilder b = new StringBuilder();
        
        for (int i = 1; i < food.length; i++){
            cal = food[i] / 2;
            for (int j =0; j < cal; j ++){
                f.append(i);
                b.append(i);
            }
            
        }
        // b = f;
        b.reverse();
        
        return f+"0"+b;
    }
}