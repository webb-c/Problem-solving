import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = s.nextInt();
    	int z=0;
    	int o=0;
    	s.nextLine();
    	
    	for(int i = 0 ; i<count ; i++) {
    		String n = s.nextLine();
    		z = 0;
    		o = 0;
    		for(int j = 0; j<n.length() ;j++) {
    			if((n.charAt(j)=='A')||(n.charAt(j)=='a')||(n.charAt(j)=='E')||(n.charAt(j)=='e')||(n.charAt(j)=='I')||(n.charAt(j)=='i')||(n.charAt(j)=='O')||(n.charAt(j)=='o')||(n.charAt(j)=='U')||(n.charAt(j)=='u')) {
    				o++;
    			}
    			else if(n.charAt(j)!=' ') {
    				z++;
    			}
    		}
    		System.out.println(z+" "+o);
    	}
 
    }
}