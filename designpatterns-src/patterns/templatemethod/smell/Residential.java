package patterns.templatemethod.smell;

public class Residential extends CapitalStrategy{

	public double getBillableAmount(){
		return getUnits()*getRate() + getBase()*getTax();
	}
	
}
