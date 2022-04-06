package br.ic.ufal.employees;

public class Hourly extends Employee {
    
    private double workingHours; 

    public Hourly(){
        
    }

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
        return  super.toString() +
                "Working Hours: " + this.getWorkingHours();
    }
 
}


