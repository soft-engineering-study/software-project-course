package br.ic.ufal.employees;
public class Commissioned extends Employee{
    
    private double commission;

    public Commissioned(String name, String address, double timeCard, double commission){

        super(name, address, timeCard);
        this.commission = commission; 

    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString()+
               "\n Commission: " + this.commission;
    }

    @Override
    public String definePayment(String paymentType) {
        // TODO Auto-generated method stub
        return null;
    }
}
