import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        
        int d = 2;
        while (n > 1) {
            if (n % d == 0) {
                if (!list.contains(d)) { 
                    list.add(d);
                }
                n /= d;
            } else {
                d++;
            }
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}