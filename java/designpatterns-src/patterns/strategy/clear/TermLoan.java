package patterns.strategy.clear;

public class TermLoan implements CapitalStrategy {

	@Override
	public double execute(Loan loan) {
		// TODO Auto-generated method stub
		return loan.outstandingRiskAmount() * 
			   loan.duration() * 
			   loan.riskFactor() +
			   loan.unusedRiskAmount() *
			   loan.duration() * 
			   loan.unusedRiskFactor();
	}

}
