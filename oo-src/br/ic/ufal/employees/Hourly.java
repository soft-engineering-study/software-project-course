package br.ic.ufal.employees;

public class Hourly extends Employee{

    private double hours; 

    public Hourly(String name, String address, double timeCard, double hours){

        super(name, address, timeCard);
        this.hours = hours; 

        

    }

    public void testando(){
        
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString()+
               "\nHours: " + this.hours;
    }
    
}
