package tantangan;
public class tantangan2no2 {
    public static void main(String [] args) {
        char jenisKelamin = 'P';
        int tinggiBadan = 160;
        int beratIdeal;
            if(jenisKelamin == 'P'){
                beratIdeal = tinggiBadan - 110;
            }
            else{
                beratIdeal = tinggiBadan - 100;
            }
        System.out.println("Jenis Kelamin " + jenisKelamin);
        System.out.println("Tinggi Badan " + tinggiBadan);
        System.out.println("Berat Ideal " + beratIdeal);
    }
}
