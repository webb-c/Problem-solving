import java.util.Scanner;

public class Main { 								 //백준 : public 없애고 Test -> Main으로 변경
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		int num;
		int i=1;
		boolean even = true;
		
		while(true) {
			/*n0*/
			num = s.nextInt();
			if(num == 0) break;
			
			/*n1*/
			num = num*3;
			//n1이 짝수
			if(num%2 == 0) {
                even = true;
				num = num/2;
			}
			//n1이 홀수
			else {
				even = false;
				num = (num+1)/2;
			}
			
			/*n3*/
			num = 3*num;
			
			/*n4*/
			num = (int)(num/9);
			
			System.out.print(i+". ");
			if(even) System.out.print("even ");
			else System.out.print("odd ");

			System.out.println(num);
			i++;
		}
	}
}
