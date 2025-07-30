package patterns.interpreter.clear;

public class BelowPriceSpec extends Specification {

	private float priceThreshold;
	
	public BelowPriceSpec(float price) {
		// TODO Auto-generated constructor stub
	}

	public void BelowPriceSpec(float priceThreshold){
		this.priceThreshold = priceThreshold;
	}
	
	@Override
	public boolean isSatisfiedBy(Product product) {
		// TODO Auto-generated method stub
		return product.getPrice() <  getPriceThreshold();
	}

	public float getPriceThreshold() {
		return priceThreshold;
	}
}
