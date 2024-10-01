import java.util.*;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int N = sc.nextInt();
       int square = 1;
       for (int i =0; i < N+1; i++){
           if ( i == 0){
               square = 1;
           }else{
               square  *= 2;
           }
       }
       System.out.print((int)Math.pow((square+1),2));
    }
}