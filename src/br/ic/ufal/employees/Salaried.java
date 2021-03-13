package br.ic.ufal.employees;

public class Salaried extends Employee{
    
    private double salary; 

    public Salaried(String name, double salary){
        super(name);
        this.salary = salary;
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }

}

