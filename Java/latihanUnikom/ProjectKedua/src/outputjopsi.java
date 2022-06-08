import javax.swing.JOptionPane;

public class outputjopsi {
    public static void main(String args []) {
        String nama = JOptionPane.showInputDialog(null, "Masukan Nama Anda : ");
        float tinggiBadan = Float.parseFloat(JOptionPane.showInputDialog(null, "Masukan Tinggi Badan Anda : "));
        
        JOptionPane.showMessageDialog(null, "Nama Saya " + nama);
        JOptionPane.showMessageDialog(null, "Usia Saya " + tinggiBadan);
    }
}
