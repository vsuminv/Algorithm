class Solution {
    public int solution(int order) {
        int answer = 0;
        String[] order_str = String.valueOf(order).split("");
        
        for (int i = 0; i < order_str.length; i++){
            if(order_str[i].contains("3") || order_str[i].contains("6") || order_str[i].contains("9")){
                answer += 1;
            }
              
        }
        return answer;
    }
}