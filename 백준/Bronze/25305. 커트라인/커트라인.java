import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int answer = 0;

        Integer[] num = new Integer[N];
        
        for (int i = 0; i < N; i++) {
            num[i] = sc.nextInt();
        }
        Arrays.sort(num , Collections.reverseOrder());
       for (int i = 0; i < M; i++) {
            answer = num[i];
        }

        
            

        System.out.print(answer);
    }
}