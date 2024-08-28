import java.util.Arrays;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr = s.split(" ");
        int[] arr_int = new int[arr.length];
        for (int i =0; i < arr.length; i++){
            arr_int[i] = Integer.parseInt(arr[i]);
        }
        
        int max = Arrays.stream(arr_int).max().getAsInt();
        int min = Arrays.stream(arr_int).min().getAsInt();
        
        
        answer = String.valueOf(min) + " " + String.valueOf(max);
        return answer;
    }
}