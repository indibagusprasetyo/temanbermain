package tantangan;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import javax.swing.JOptionPane;

public class tantangan2input {
    public static void main(String args []) throws IOException{
            BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
            //input
            System.out.println("Masukan Panjang Alas : ");
            float alas = Float.parseFloat(input.readLine());

            System.out.println("Masukan Tinggi : ");
            float tinggi = Float.parseFloat(input.readLine());

            int luas = (int) ((alas*tinggi) / 2);
            //output
            JOptionPane.showMessageDialog(null, "Luas :" + luas);
    }
}
