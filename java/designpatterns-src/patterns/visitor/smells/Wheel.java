package patterns.visitor.smells;

public class Wheel implements CarElement {

	@Override
	public void print(String activity) {
		System.out.println("Wheel: "+activity);
	}
}
