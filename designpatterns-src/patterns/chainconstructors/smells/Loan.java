package patterns.chainconstructors.smells;

import java.util.Date;

public class Loan {
	
	private CapitalStrategy strategy;
	private float notional;
	private float outstanding;
	private int rating;
	private Date expiry;
	private Date maturity;
	
	public Loan(float notional, float outstanding, int rating, Date expiry){
		this.strategy = new TermROC();
        this.notional = notional;
        this.outstanding = outstanding;
        this.rating = rating;
        this.expiry = expiry;
	}
	
	public Loan(float notional, float outstanding, int rating, Date expiry, Date maturity){
		this.strategy = new RevolvingTermROC();
        this.notional = notional;
        this.outstanding = outstanding;
        this.rating = rating;
        this.expiry = expiry;
        this.maturity = maturity;
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
