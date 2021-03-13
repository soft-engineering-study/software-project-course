package br.ic.ufal.ifs; 

import java.util.Scanner;

public class Comparison {

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

        System.out.println(number1 == 3 ? "Valor correto" : "Valor Errado");

        if(number1 == number2) 
            if(number1 == 2)
                System.out.printf("%d == %d%n", number1, number2);
        else if(number1 != number2)
            System.out.printf("%d != %d%n", number1, number2);
        else if(number1 < number2)
            System.out.printf("%d < %d%n", number1, number2);
        else if(number1 > number2)
            System.out.printf("%d > %d%n", number1, number2);
        else if(number1 <= number2)
            System.out.printf("%d <= %d%n", number1, number2);
        else if(number1 >= number2)
            System.out.printf("%d >= %d%n", number1, number2);

    }

}
