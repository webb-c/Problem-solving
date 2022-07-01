import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int n1 = s.nextInt();
    	int n2 = s.nextInt();
    	int n3 = s.nextInt();
    	int trim;
    	
    	if(n1<n3) {
    		trim = n1;
    		n1 = n3;
    		n3 = trim;
    	}
    	if(n1<n2) {
    		trim = n1;
    		n1 = n2;
    		n2 = trim;
    	}
    	if(n2<n3) {
    		trim = n2;
    		n2 = n3;
    		n3 = trim;
    	}
    	
    	System.out.println(n2);
 
    }
}