import java.util.Scanner;

public class nestloop {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input jumlah rangakaian :");
        int x = input.nextInt();

        for (int a = 1; a <= x; a++) {
            for (int b = 1; b <= x; b++) {
                System.out.print(b + " ");
            }
            System.out.println(" ");
        }
    }
}
