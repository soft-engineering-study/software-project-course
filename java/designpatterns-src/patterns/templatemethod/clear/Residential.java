package patterns.templatemethod.clear;

public class Residential extends CapitalStrategy{

	@Override
	public double getBaseAmount() {
		return getUnits()*getRate();
	}

	@Override
	public double getTaxAmount() {
		return getBase()*getTax();
	}
	
}
