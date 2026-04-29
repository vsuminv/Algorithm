class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] arr = my_string.split("");

        for(int i =0; i < arr.length; i++){
            if (answer.contains(arr[i])){
                continue;
            }
            answer += arr[i];
        }
        return answer;
    }
}