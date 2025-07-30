package patterns.templatemethod.smell;

public class Lifeline extends CapitalStrategy{

	public double getBillableAmount(){
		return getUnits()*getRate()*0.5 + getBase()*getTax()*0.2;
	}
}
