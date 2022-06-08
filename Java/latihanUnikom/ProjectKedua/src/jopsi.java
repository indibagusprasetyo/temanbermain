import javax.swing.JOptionPane;

public class jopsi {
    public static void main(String args []) {
        String nama = "Indi";
        short usia = 20;
        char goldar = 'O';
        float tinggiBadan = 171.922f;
        
        JOptionPane.showMessageDialog(null, "Nama Saya " + nama);
        JOptionPane.showMessageDialog(null, "Usia Saya " + usia);
        JOptionPane.showMessageDialog(null, "Golongan Darah " + goldar + "\n" + "Tinggi Badan " + tinggiBadan);
    }
}
