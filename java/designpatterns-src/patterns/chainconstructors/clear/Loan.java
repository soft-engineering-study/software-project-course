package patterns.chainconstructors.clear;

import java.util.Date;

public class Loan {
	
	private CapitalStrategy strategy;
	private float notional;
	private float outstanding;
	private int rating;
	private Date expiry;
	private Date maturity;
	
	public Loan(float notional, float outstanding, int rating, Date expiry){
		this(new TermROC(), notional, outstanding, rating, expiry, null);
	}
	
	public Loan(float notional, float outstanding, int rating, Date expiry, Date maturity){
		this(new RevolvingTermROC(), notional, outstanding, rating, expiry, maturity);
	}
	
	public Loan(CapitalStrategy strategy, float notional, float outstanding, int rating, Date expiry, Date maturity){
		this.strategy = strategy;
        this.notional = notional;
        this.outstanding = outstanding;
        this.rating = rating;
        this.expiry = expiry;
        this.maturity = maturity;
	}
}
