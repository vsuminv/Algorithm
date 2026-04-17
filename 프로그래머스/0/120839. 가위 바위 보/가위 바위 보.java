class Solution {
    public String solution(String rsp) {
        String answer = "";
        String[] rsp_list = rsp.split("");
        for(int i = 0; i < rsp_list.length; i++){
            if (rsp_list[i].equals("0")){
                answer += "5";
            }else if(rsp_list[i].equals("2")){
                answer += "0";
            }else{
                answer += "2";
            }
        }
        
  
        return answer;
    }
}