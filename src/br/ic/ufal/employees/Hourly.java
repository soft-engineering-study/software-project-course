package br.ic.ufal.employees;

public class Hourly extends Employee{
    
    private double workingHours; 

    public Hourly(String name, double workingHours){
        super(name);
        this.workingHours = workingHours;
    }

    public double getWorkingHours() {
        return workingHours;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return  this.getWorkingHours() + ":" +
                super.getName();
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }
 
}


