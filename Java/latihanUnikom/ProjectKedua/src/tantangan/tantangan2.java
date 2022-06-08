package tantangan;
public class tantangan2 {
    public static void main(String[] args) {
        short nilai = 50;
        char index;
        index = nilai >= 80 ? 'A' : nilai >= 70 ? 'B' : nilai >= 60 ? 'C': 'D';
        
        System.out.println("Nilai: " + nilai);
        System.out.println("Index: " + index);
    }
}
