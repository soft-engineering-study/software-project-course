
import java.util.Scanner;

public class AccountTest {

    public static void main(String[] args) {

//        Version 1
//        // Create a scanner to obtain the input from the command line
//        Scanner input = new Scanner(System.in);
//
//        // Create an account object and assign it to myAccount
//        Account myAccount = new Account();
//
//        // display the initial value of name (null)
//        System.out.printf("Initial name is: %s%n%n", myAccount.getName());
//
//        System.out.println("Please enter the name: ");
//        String theName = input.nextLine(); // read a line of text
//        myAccount.setName(theName); //  put theName in myAccount
//        System.out.println(); // outputs a blank line
//
//        // display the name stored in object myAccount
//        System.out.printf("Name in object myAccount is: %n%s%n", myAccount.getName());

//        Version 2
//        // Create two Account objects
//        Account account1 = new Account("Jane Green");
//        Account account2 = new Account("John Blue");
//
//        // display initial value of name for each account
//        System.out.printf("account1 name is: %s%n", account1.getName());
//        System.out.printf("account2 name is: %s%n", account2.getName());

//        Version 3
//        Account account1 = new Account("Jane Green");
//        Account account2 = new Account("John Blue");
//
//        // display the initial balance of each object
//        System.out.printf("%s balance: $%.2f%n", account1.getName(), account1.getBalance());
//        System.out.printf("%s balance: $%.2f%n", account2.getName(), account2.getBalance());
//
//        // Create a scanner to obtain the input from the command line
//        Scanner input = new Scanner(System.in);
//
//        System.out.println("Enter the deposit amount for account1: "); // prompt
//        double depositAmount = input.nextDouble();
//        System.out.printf("%n adding %.2f to account balance %n%n", depositAmount);
//        account1.deposit(depositAmount);
//
//        // display balances
//        System.out.printf("%s balance: $%.2f%n", account1.getName(), account1.getBalance());
//        System.out.printf("%s balance: $%.2f%n", account2.getName(), account2.getBalance());
//
//        System.out.println("Enter the deposit amount for account2: "); // prompt
//        depositAmount = input.nextDouble();
//        System.out.printf("%n adding %.2f to account balance %n%n", depositAmount);
//        account2.deposit(depositAmount);
//
//        // display balances
//        System.out.printf("%s balance: $%.2f%n", account1.getName(), account1.getBalance());
//        System.out.printf("%s balance: $%.2f%n", account2.getName(), account2.getBalance());

        Account account1; 

        // display the initial balance of each object
        displayAccount(account1);
        displayAccount(account2);

        // Create a scanner to obtain the input from the command line
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the deposit amount for account1: "); // prompt
        double depositAmount = input.nextDouble();
        System.out.printf("%n adding %.2f to account balance %n%n", depositAmount);
        account1.deposit(depositAmount);

        // display balances
        displayAccount(account1);
        displayAccount(account2);

        System.out.println("Enter the deposit amount for account2: "); // prompt
        depositAmount = input.nextDouble();
        System.out.printf("%n adding %.2f to account balance %n%n", depositAmount);
        account2.deposit(depositAmount);

        // display balances
        displayAccount(account1);
        displayAccount(account2);

    }

    public static void displayAccount(Account accountToDisplay) {
        System.out.printf("%s balance: $%.2f%n", accountToDisplay.getName(), accountToDisplay.getBalance());
    }

}
