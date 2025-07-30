package patterns.strategy.clear;

public class Loan {
	
	private CapitalStrategy capitalStrategy;
	private int commitment;
	
	public Loan(CapitalStrategy capitalStrategy) {
		// TODO Auto-generated constructor stub
		this.capitalStrategy = capitalStrategy;
	}
	
	public double capital(){
		return capitalStrategy.execute(this);
	}
	
	public double unusedRiskFactor() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double unusedRiskAmount() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double outstandingRiskAmount() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double getUnusedPercentage() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double duration() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double riskFactor() {
		// TODO Auto-generated method stub
		return 0;
	}
	
	public int getCommitment() {
		return commitment;
	}
}
