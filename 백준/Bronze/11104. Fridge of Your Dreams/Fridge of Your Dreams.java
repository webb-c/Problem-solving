import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	
    	int count = s.nextInt();
    	s.nextLine();
    	
    	for(int i = 0 ; i<count ; i++) {
    		String n = s.nextLine();
    		int num = Integer.parseInt(n, 2);
    		System.out.println(num);
    	}
 
    }
}
