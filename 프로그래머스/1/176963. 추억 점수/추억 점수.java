import java.util.*;

class Solution {
    public List<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> dic = new HashMap<>();
        
        for (int i = 0; i < name.length; i++) {
            dic.put(name[i], yearning[i]);
        }
        

        for (String[] row : photo) {
            int total = 0;
            for (String names : row) {
                if (dic.containsKey(names)) {
                    total += dic.get(names);
                }
            }
            answer.add(total);
        }
        
        return answer;
    }
}
