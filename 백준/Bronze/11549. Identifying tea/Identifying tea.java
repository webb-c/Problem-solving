import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int set = s.nextInt();
    	int count = 0;
    	
    	for(int i = 0 ; i < 5 ; i++) {
    		int num = s.nextInt();
    		if(num == set) count++;
    	}
    	
    	System.out.println(count);
    }
}