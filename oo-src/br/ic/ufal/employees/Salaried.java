package br.ic.ufal.employees;

public class Salaried extends Employee {
    
    private double salary;

    public Salaried(String name, String address, double timeCard, double salary){

        super(name, address, timeCard);
        this.salary = salary; 

    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString()+
               "\nSalary: " + this.salary;
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }
}
