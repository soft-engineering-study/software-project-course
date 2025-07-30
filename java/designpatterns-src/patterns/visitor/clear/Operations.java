package patterns.visitor.clear;

public class Operations {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Car car = new Car();
	        car.accept(new CarElementPrintVisitor());
	        car.accept(new CarElementDoVisitor());
	}

}
