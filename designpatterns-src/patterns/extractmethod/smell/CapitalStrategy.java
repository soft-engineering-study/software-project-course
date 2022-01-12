package patterns.extractmethod.smell;

import patterns.extractmethod.Loan;;

public class CapitalStrategy {

	public double advisedLine(Loan loan){
		return loan.getUnusedPercentage()*
			   loan.getCommitment()*
	           duration(loan);

	}

	public double termLoan(Loan loan) {
		return loan.getCommitment()*
		       duration(loan)*
		       riskFactFor(loan);
	}
	
	private int riskFactFor(Loan loan) {
		// TODO Auto-generated method stub
		return 0;
	}

	private int duration(Loan loan) {
		// TODO Auto-generated method stub
		return 0;
	}
	
}
