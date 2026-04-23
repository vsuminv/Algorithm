class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] my_string_list = my_string.split("");
        for (int i =0; i < my_string_list.length; i++){
            if (my_string_list[i].equals("a") ||my_string_list[i].equals("e") || my_string_list[i].equals("i") || my_string_list[i].equals("o")|| my_string_list[i].equals("u")){
                continue;
                
            }else{
                answer+=my_string_list[i];
            }
        }
        return answer;
    }
}