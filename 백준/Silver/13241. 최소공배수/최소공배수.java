import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        long r = a * b;
        long tmp = 0;
        long max = 0;
        while(b !=0){
            a = a % b;
            tmp = a;
            a = b;
            b = tmp;
        }
        max = a;
        System.out.println(r / max);
    }
}