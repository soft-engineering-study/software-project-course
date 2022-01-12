package patterns.visitor.smells;

public class Engine implements CarElement {

	@Override
	public void print(String activity) {
		System.out.println("Engine: "+activity);
	}
}
