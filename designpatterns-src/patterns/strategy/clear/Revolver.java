package patterns.strategy.clear;

public class Revolver implements CapitalStrategy {

	@Override
	public double execute(Loan loan) {
		// TODO Auto-generated method stub
		return loan.getCommitment() * 
				   loan.getUnusedPercentage() * 
				   loan.duration() * 
				   loan.riskFactor();
	}

}
