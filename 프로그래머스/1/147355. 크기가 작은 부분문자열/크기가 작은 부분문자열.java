class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int tLength = t.length();
        int pLength = p.length();

        
        for (int i = 0; i <= tLength - pLength; i++) {
            String substring = t.substring(i, i + pLength);
            if (substring.compareTo(p) <= 0) {
                answer++;
            }
        }

        return answer;
    }
}