class Solution {
    public String solution(String my_string, int num1, int num2) {
        String[] s_list = my_string.split("");
        String answer = "";
        
        String n1 = s_list[num1];
        String n2 = s_list[num2];
        s_list[num1]= n2;
        s_list[num2]= n1;
        
        return String.join("", s_list);
    }
}