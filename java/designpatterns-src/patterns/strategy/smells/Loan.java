package patterns.strategy.smells;

public class Loan {
	
	private Expiry expiry = null;
	private Maturity maturity = null;
	private int commitment;
	
	public Loan() {
		// TODO Auto-generated constructor stub
	}
	
	public Loan(Expiry expiry) {
		// TODO Auto-generated constructor stub
		this.expiry = expiry;
	}
	
	public Loan(Maturity maturity) {
		// TODO Auto-generated constructor stub
		this.maturity = maturity;
	}
	
	public Loan(Expiry expiry, Maturity maturity) {
		// TODO Auto-generated constructor stub
		this.expiry = expiry;
		this.maturity = maturity;
	}

public double capital(){
	
	if (expiry == null && maturity != null) {
		return commitment * duration() * riskFactor();
	}else if (expiry == null && 
			  maturity == null &&
			  getUnusedPercentage() != 1) {
		return commitment * 
			   getUnusedPercentage() * 
			   duration() * 
			   riskFactor();
	}else {
		return outstandingRiskAmount() * 
			   duration() * 
		       riskFactor() +
		       unusedRiskAmount() *
		       duration() * 
		       unusedRiskFactor();
	}
}

	private double unusedRiskFactor() {
		// TODO Auto-generated method stub
		return 0;
	}

	private double unusedRiskAmount() {
		// TODO Auto-generated method stub
		return 0;
	}

	private double outstandingRiskAmount() {
		// TODO Auto-generated method stub
		return 0;
	}

	private double getUnusedPercentage() {
		// TODO Auto-generated method stub
		return 0;
	}

	private double duration() {
		// TODO Auto-generated method stub
		return 0;
	}

	private double riskFactor() {
		// TODO Auto-generated method stub
		return 0;
	}
}
