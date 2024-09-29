import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();

        List<Integer> sosu_list = new ArrayList<>();
        
        for (int num = M; num <= N; num++) {
            int count = 0;
            if (num > 1) {
                for (int i = 2; i < num; i++) {
                    if (num % i == 0) {
                        count += 1;
                        break;
                    }
                }
                if (count == 0) {
                    sosu_list.add(num);
                }
            }
        }

        if (sosu_list.size() > 0) {
            int sum = 0;
            int min = sosu_list.get(0);

            for (int prime : sosu_list) {
                sum += prime;
                if (prime < min) {
                    min = prime;
                }
            }

            System.out.println(sum);
            System.out.println(min);
        } else {
            System.out.println(-1);
        }

        sc.close();
    }
}
