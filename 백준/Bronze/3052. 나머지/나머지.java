import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> num = new HashSet<>();
        int a = 0;
        for (int i = 0; i < 10; i++){
            a = sc.nextInt();
            num.add(a%42);
        }
        
        System.out.println(num.size());
    }
}