import br.ic.ufal.entities.Employee;

public class Commissioned extends Employee{
    
    private double commission; 

    public Commissioned(String name, double commission){
        super(name);
        this.commission = commission;
    }
}

