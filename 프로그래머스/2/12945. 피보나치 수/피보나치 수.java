class Solution {
    public int solution(int n) {
        // if (n == 0) return 0;
        // if (n == 1) return 1;
        
        long[] n_list = new long[n + 1];
        n_list[0] = 0;
        n_list[1] = 1;

        for (int i = 2; i <= n; i++) {
            n_list[i] = (n_list[i - 1] + n_list[i - 2]) % 1234567;
        }
        
        return (int) n_list[n];
    }
}
