import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for(int i=1; i < n+1; i++){
            for (int j =0; j<i-1; j++){
                System.out.print(" ");
            }
            for (int k =i; k<n+1; k++){
                System.out.print("*");
            }
            System.out.println();
        }
        
        
    }
}