package br.ic.ufal.employees;

public class Commissioned extends Employee{
    
    private double commission; 

    public Commissioned(String name, double commission){
        super(name);
        this.commission = commission;
    }

   
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString()+ 
               "Commission: " + this.commission;
    }
}

