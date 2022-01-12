package patterns.visitor.clear;

public class CarElementDoVisitor implements CarElementVisitor {

	@Override
	public void visit(Wheel wheel) {
		// TODO Auto-generated method stub
		System.out.println("Kicking my " + wheel.getName() + " wheel");
	}

	@Override
	public void visit(Engine engine) {
		// TODO Auto-generated method stub
		System.out.println("Starting my engine");
	}

	@Override
	public void visit(Body body) {
		// TODO Auto-generated method stub
		System.out.println("Moving my body");
	}

	@Override
	public void visit(Car car) {
		// TODO Auto-generated method stub
		System.out.println("Starting my car");
	}

}
