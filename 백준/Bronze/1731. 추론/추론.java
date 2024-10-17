import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] r = new int[N];
        int  result = 0;
        for(int i = 0; i < N; i++){
            r[i] = sc.nextInt();
        }
        
        int x = r[1] - r[0]; 
        int x1 = r[1] / r[0]; 
        
        for (int i = 2; i < N; i++){
            if (r[i] - r[i-1] == x){
                result = r[N-1] + x;
            }else{
                if (r[i] / r[i-1] == x1){
                    result = r[N-1] * x1;
                }
            }
        }
        
        System.out.print(result);
    }
}