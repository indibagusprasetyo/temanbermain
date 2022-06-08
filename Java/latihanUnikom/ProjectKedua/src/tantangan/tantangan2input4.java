package tantangan;
import javax.swing.JOptionPane;

public class tantangan2input4 {
    public static void main(String [] args) {
        String jk = JOptionPane.showInputDialog(null, "Jenis Kelamin : ");
        int tinggiBadan = Integer.parseInt(JOptionPane.showInputDialog(null, "Masukan Tinggi Badan Anda : "));
        int beratIdeal = 0;
            if("P".equals(jk)){ 
                beratIdeal = tinggiBadan - 110;
            }
            else if("L".equals(jk)){
                beratIdeal = tinggiBadan - 100;
            }
        
        JOptionPane.showMessageDialog(null, "Jenis Kelamin : " + jk + "\nTinggi Badan Anda : " + tinggiBadan + "\nBerat yang ideal untuk Anda : " + beratIdeal);
        }
}
