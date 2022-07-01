import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = s.nextInt();
    	for(int i = 0 ; i<count ; i++) {
    		String name = s.next();
    		int num = s.nextInt();
    		
    		if(97 <= num && num <= 100) {
    			System.out.println(name+" A+");
    		}
    		else if(90 <= num && num <= 96) {
    			System.out.println(name+" A");
    		}
    		else if(87 <= num && num <= 89) {
    			System.out.println(name+" B+");
    		}
    		else if(80<= num && num <= 86) {
    			System.out.println(name+" B");
    		}
    		else if(77<= num && num <= 79) {
    			System.out.println(name+" C+");
    		}
    		else if(70<= num && num <= 76) {
    			System.out.println(name+" C");
    		}
    		else if(67 <= num && num <= 69) {
    			System.out.println(name+" D+");
    		}
    		else if(60 <= num && num <= 66) {
    			System.out.println(name+" D");
    		}
    		else {
    			System.out.println(name+" F");
    		}
    	}
    }
}