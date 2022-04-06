package br.ic.ufal.employees;

public class Salaried extends Employee{
    
    private double salary; 

    public Salaried(String name, double salary){
        super(name);
        this.salary = salary;
    }

   
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString()+ 
               "Salary: " + this.salary;
    }
}

