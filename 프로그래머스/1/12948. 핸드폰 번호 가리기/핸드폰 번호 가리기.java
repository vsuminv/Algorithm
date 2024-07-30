class Solution {
    public String solution(String phone_number) {
      int length = phone_number.length();
      int maskLength = length - 4;
       StringBuilder maskedPart = new StringBuilder();
        for (int i = 0; i < maskLength; i++) {
            maskedPart.append('*');
        }
        String lastFourDigits = phone_number.substring(length - 4);
        String answer = maskedPart.toString() + lastFourDigits;
      return  answer;
    }
}