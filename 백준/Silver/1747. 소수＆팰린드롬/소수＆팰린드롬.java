import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int num = s.nextInt(); //int로 저장
    	int i = num;
    	boolean check = false;
    	
    	while(true) {
    		
    		List<String> list = new ArrayList();
        	List<String> list_r = new ArrayList();
    		
    		String i_str = Integer.toString(i);  //i를 문자열 형태로 받음
    		for(int k = 0 ; k < i_str.length() ; k++) {
    			list.add(Character.toString(i_str.charAt(k)));
    		}
    		
    		String str = list.toString();
    		list_r = list;
    		Collections.reverse(list_r);
    		String str_r = list_r.toString();
    		
    		//뒤집은 숫자가 기존 숫자와 동일할 때
    		if(0==str.compareTo(str_r)) { 

    			/*소수 판별 작업*/
    			for(int l = 2 ; l <= i/2 ; l++) {
    				if(i%l == 0) {
    					check = false;
    					break;
    				}
    				else {
    					check = true;
    				}
    			}
                
                if( i==2 || i==3 ) check = true;
    			
    			if(check) {
    				System.out.println(i);
    				break;
    			}
    		}
    		
    		i++;   //다를경우 i를 1증가하고 반복
    	}
    }
}