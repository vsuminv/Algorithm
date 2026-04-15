class Solution {
    public String solution(int age) {
        String answer = "";
        String[] alpha = {"a","b","c","d","e","f","g","h","i","j"};
        String str = new String(age + "");
        String strArr[] = str.split("");
        
        for (int j = 0; j < strArr.length; j++){
            for(int i = 0; i < alpha.length; i++){
                if (strArr[j].equals(String.valueOf(i))){
                    answer += alpha[i];
                }
            
            }
                
                
        }
        
        
       
        
        return answer;
    }
}