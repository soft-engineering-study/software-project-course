package br.ic.ufal.employees;

public class Commissioned extends Employee{
    
    private double commission; 

    public Commissioned(String name, double commission){
        super(name);
        this.commission = commission;
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }
}

