package tantangan;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class tantangan2input2 {
    public static void main(String args []) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Masukan Nama Nomor A :");
        int angka1 = Integer.parseInt(input.readLine());

        System.out.print("Masukan Nama Nomor B :");
        int angka2 = Integer.parseInt(input.readLine());

        String angkaout = angka1 > angka2 ? "Nilai A lebih besar dar B" : angka1 < angka2 ? "Nilai A lebih kecil dari B" : "Nilai A dan B sama besar" ;
        System.out.println(angkaout);
        }
    }