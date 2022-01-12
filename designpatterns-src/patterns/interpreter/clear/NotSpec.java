package patterns.interpreter.clear;

public class NotSpec extends Specification {

	private Specification specToNegate;
	
	public NotSpec(Specification specToNegate) {
		// TODO Auto-generated constructor stub
		this.specToNegate = specToNegate;
	}
	
	@Override
	public boolean isSatisfiedBy(Product product) {
		// TODO Auto-generated method stub
		return !specToNegate.isSatisfiedBy(product);
	}

}
