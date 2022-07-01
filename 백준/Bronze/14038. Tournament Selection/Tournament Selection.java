import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = 0;
    	
    	for(int i = 0 ; i<6 ; i++) {
    		char c = s.nextLine().charAt(0);
    		if(c=='W') count++;
    	}
    	
    	if(4<count && count<=6) System.out.println("1");
    	else if(2<count && count<=4) System.out.println("2");
    	else if(1<=count && count<=2) System.out.println("3");
    	else System.out.println("-1");
    }
}