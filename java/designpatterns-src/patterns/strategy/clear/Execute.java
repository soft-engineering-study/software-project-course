package patterns.strategy.clear;

public class Execute {
	public static void main(String[] args) {
		Loan loan = new Loan(new AdvisedLine());
		System.out.println(loan.capital());
	}
}
