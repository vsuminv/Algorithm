class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] my_string_list = my_string.split("");
        for (int i = 0; i < my_string_list.length; i++){
            if(my_string_list[i].equals(my_string_list[i].toUpperCase())){
                answer += my_string_list[i].toLowerCase();
            }else{
                answer += my_string_list[i].toUpperCase();
            }
        }
        return answer;
    }
}