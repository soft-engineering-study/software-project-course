
public class EnhancedForTest {
    public static void main(String[] args) {
        int[] array = {32,27,64,18,95,14,90,70,60,37};
        int total = 0;
        
        for(int number : array)
            total += number;

        System.out.printf("Total of array elements: %d%n", total);
    }
}
