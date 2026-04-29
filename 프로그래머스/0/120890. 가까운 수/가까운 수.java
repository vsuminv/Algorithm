class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;

        int[] diffArr = new int[array.length];

    
        for (int i = 0; i < array.length; i++) {
            diffArr[i] = Math.abs(n - array[i]);
        }

    
        int min = diffArr[0];
        for (int i = 1; i < diffArr.length; i++) {
            if (diffArr[i] < min) {
                min = diffArr[i];
            }
        }


        answer = Integer.MAX_VALUE;

        for (int i = 0; i < diffArr.length; i++) {
            if (diffArr[i] == min) {
                if (array[i] < answer) {
                    answer = array[i];
                }
            }
        }

        return answer;
    }
}