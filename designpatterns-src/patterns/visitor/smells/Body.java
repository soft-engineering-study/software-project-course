package patterns.visitor.smells;

public class Body implements CarElement {

	@Override
	public void print(String activity) {
		System.out.println("Body:" + activity);
	}
}
