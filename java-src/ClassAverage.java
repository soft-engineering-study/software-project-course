
import java.util.Scanner;

public class ClassAverage {

    public static void main(String[] args) {
        // Create a scanner to obtain the input from the command line
        Scanner input = new Scanner(System.in);

        // initialization phase
        int total = 0;
        int gradeCounter = 1;

        while (gradeCounter <= 10) {
            System.out.println("Enter grade: "); // prompt
            int grade = input.nextInt(); // input next grade
            total = total + grade; // add grade to total
            gradeCounter = gradeCounter + 1; // increment counter by 1
        }

        // termination phase
        int average = total / 10;

        // display total and average of grades
        System.out.printf("%n Total of all 10 grades is %d%n", total);
        System.out.printf("Class average is %d%n", average);

    }
}
