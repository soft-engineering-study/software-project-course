// Addition program that input two numbers and then display the sum

import java.util.Scanner; // This program use the class scanner

public class Addition {

    public static void main(String[] args) {

        // Create a scanner to obtain the input from the command line
        Scanner input = new Scanner(System.in);

        int number1; // first number to add
        int number2; // second number to add
        int sum; // sum of number1 and number2

        System.out.println("Enter the first integer: "); // prompt
        number1 = input.nextInt();

        System.out.println("Enter the second integer: "); // prompt
        number2 = input.nextInt();

        sum = number1 + number2;

        System.out.printf("Sum is %d%n", sum); // display Sum

    }

}
