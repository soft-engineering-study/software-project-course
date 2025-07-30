

public class Account {

    public Address address;    
    public String name; // instance variable
    public int balance; // instance variable

    // Empty Constructor
    public Account() {
        System.out.println("kkkkkk");
        
    }

    // Constructor receiving the name
    public Account(String name) {
        this.name = name;
    }

    public Account(String name, double balance) {
        this.name = name;

        if (balance > 0.0)
            this.balance = balance;
    }


    // method that deposit (adds) only a valid amount to the balance
    public void deposit(double depositAmount) {
        if (depositAmount > 0.0) // if the depositAmount is valid
            balance = balance + depositAmount; // add it to the balance
    }

    // returns the account balance
    public double getBalance() {
        return balance;
    }

    // method to set the name in the object
    public void setName(String name) {
        this.name = name;
    }

    // method to retrieve the name from the object
    public String getName() {
        return name;
    }

}
