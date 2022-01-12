package patterns.interpreter.clear;

public class AndSpec extends Specification{

	private Specification augend, addend;
	
	public AndSpec(Specification augend, Specification addend) {
		// TODO Auto-generated constructor stub
		this.augend = augend;
		this.addend = addend;
	}
	
	public Specification getAddend() {
		return addend;
	}
	
	public Specification getAugend() {
		return augend;
	}

	@Override
	public boolean isSatisfiedBy(Product product) {
		// TODO Auto-generated method stub
		return getAugend().isSatisfiedBy(product) && getAddend().isSatisfiedBy(product);
	}
}
