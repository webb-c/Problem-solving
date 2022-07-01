import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	int antenna=0;
    	int eyes=0;
        Scanner s = new Scanner(System.in);
        antenna=s.nextInt();
        eyes=s.nextInt();
        
        if(antenna>=3 && eyes<=4) System.out.println("TroyMartian");
        if(antenna<=6 && eyes>=2) System.out.println("VladSaturnian");
        if(antenna<=2 && eyes<=3) System.out.println("GraemeMercurian");
    }
}