import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int n = 0;
        
        List<Integer> result = new ArrayList<>();
        while(n != -1){
            n = sc.nextInt ();
            int sum = 0;
            if (n == -1) break;
            for (int i =1; i<n; i++){
                if(n % i == 0){
                    result.add(i);
                    sum += i;
                }
            }
            
            if (n == sum){
                System.out.print(n + " = " );
                for (int i =0; i <result.size(); i++){
                    
                
                    if ( result.get(i) != result.get(result.size()-1)){
                        System.out.print( result.get(i) + " + ");
                    }
                    else{
                        System.out.println( result.get(i));
                    }
                }
                
            }
            else{
                System.out.println(n + " is NOT perfect.");
            }
            result = new ArrayList<>();
        }
	}
}