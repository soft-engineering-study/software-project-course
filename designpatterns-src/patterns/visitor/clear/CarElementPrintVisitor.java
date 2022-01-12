package patterns.visitor.clear;

public class CarElementPrintVisitor implements CarElementVisitor {

	@Override
	public void visit(Wheel wheel) {
		// TODO Auto-generated method stub
		System.out.println("Visiting " + wheel.getName() + " wheel");
	}

	@Override
	public void visit(Engine engine) {
		// TODO Auto-generated method stub
		System.out.println("Visiting engine");
	}

	@Override
	public void visit(Body body) {
		// TODO Auto-generated method stub
		System.out.println("Visiting body");
	}

	@Override
	public void visit(Car car) {
		// TODO Auto-generated method stub
		System.out.println("Visiting car");
	}

}
