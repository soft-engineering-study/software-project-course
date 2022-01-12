package patterns.interpreter.clear;

public class ColorSpec extends Specification{

	private Color colorOfProductToFind; 
	
	public ColorSpec(Color colorOfProductToFind2) {
		// TODO Auto-generated constructor stub
	}

	public void ColorSpec(Color colorOfProductToFind){
		this.colorOfProductToFind = colorOfProductToFind;
	}
	
	public Color getColorOfProductToFind(){
		return colorOfProductToFind;
	}
	
	@Override
	public boolean isSatisfiedBy(Product product) {
		return product.getColor().equals(getColorOfProductToFind());
	}
}

