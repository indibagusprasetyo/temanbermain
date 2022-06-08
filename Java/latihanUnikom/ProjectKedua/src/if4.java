import java.util.Scanner;

public class if4 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int bil=0;

        do {
            System.out.print("Input angka : ");
            bil = input.nextInt();

            if(bil > 0) System.out.println("Bilangan Positif");
            else if(bil < 0) System.out.println("Bilangan Negatif");
            else System.out.println("Menutup Aplikasi");
        } while(bil != 0);
    }
}
