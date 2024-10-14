import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        int[] s = new int[n]; 
        for (int i = 0; i < n; i++) {
            s[i] = sc.nextInt();
        }
        
        int cnt = 0;

        for (int i : s) {
            if (i == 1) {
                continue; 
            }
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false; 
                    break; 
                }
            }
            if (isPrime) {
                cnt++; 
            }
        }

        System.out.println(cnt); 
    }
}
