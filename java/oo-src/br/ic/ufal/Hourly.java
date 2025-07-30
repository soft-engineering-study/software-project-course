package br.ic.ufal;

import br.ic.ufal.employees.Employee;

public class Hourly extends Employee{

    private double workingHours; 

    public Hourly(String name, String address, double timeCard, double workingHours){

        super(name, address, timeCard);
        this.workingHours = workingHours; 

        Employee employee = new Employee();
        

    }

    public double getWorkingHours() {
        return workingHours;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        

        return super.toString()+
               "\nWorking Hours: " + this.workingHours;
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }
    
    
}
