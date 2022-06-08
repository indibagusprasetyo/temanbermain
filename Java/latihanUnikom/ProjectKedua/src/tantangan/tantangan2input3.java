package tantangan;
import java.util.Scanner;

public class tantangan2input3 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukan Nilai Transaksi : ");

        int trans = input.nextInt();
        float pajak = trans > 250 ? (float) 1f : (float) 0.1f;
        float hasilpajak = trans * (pajak/100);
        float totrans = hasilpajak + trans;
        
        System.out.println("TRANSAKSI ANDA : " + trans + "\nPAJAK ANDA : " + pajak + "\nTOTAL TRANSAKSI : " + totrans);
    }   
}