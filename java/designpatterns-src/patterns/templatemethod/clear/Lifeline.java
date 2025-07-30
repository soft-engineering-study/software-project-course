package patterns.templatemethod.clear;

public class Lifeline extends CapitalStrategy{

	
	
	@Override
	public double getBaseAmount() {
		return getUnits()*getRate()*0.5;
	}

	@Override
	public double getTaxAmount() {
		return getBase()*getTax()*0.2;
	}
}
