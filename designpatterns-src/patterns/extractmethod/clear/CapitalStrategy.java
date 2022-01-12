package patterns.extractmethod.clear;

import patterns.extractmethod.Loan;

public class CapitalStrategy {

	public double advisedLine(Loan loan){
		return loan.getUnusedPercentage()*
			   deadlineLoan(loan);
	}

	public double termLoan(Loan loan) {
		return deadlineLoan(loan)*
		       riskFactFor(loan);
	}
	
	private int riskFactFor(Loan loan) {

		return 0;
	}

	private int duration(Loan loan) {

		return 0;
	}
	
	private double deadlineLoan(Loan loan){
		return loan.getCommitment()*
			       duration(loan);
	}
	
}
