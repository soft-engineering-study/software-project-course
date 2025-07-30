package patterns.strategy.clear;

public class AdvisedLine implements CapitalStrategy {

	@Override
	public double execute(Loan loan) {
		// TODO Auto-generated method stub
		return loan.getCommitment() * 
			   loan.duration() * 
			   loan.riskFactor();
	}

}
