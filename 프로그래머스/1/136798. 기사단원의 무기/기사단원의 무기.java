class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            int c = 0;
            for (int j = 1; j <= Math.sqrt(i); j++) { 
                if (i % j == 0) {
                    c += 1;
                    if (j != i / j) {
                        c += 1;
                    }
                }
            }
            if (c > limit) {
                answer += power;
            } else {
                answer += c;
            }
        }
        return answer;
    }
}
