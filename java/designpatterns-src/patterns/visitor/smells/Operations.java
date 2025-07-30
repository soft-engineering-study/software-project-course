package patterns.visitor.smells;

public class Operations {
	public static void main(String[] args) {
		Car car = new Car();
		
		for (CarElement element : car.getElements()) {
			if (element instanceof Wheel) {
				Wheel wheel = (Wheel) element;
				wheel.print("Constructing left");
			}if (element instanceof Body) {
				Body body = (Body) element;
				body.print("Constructing Body");
			}if (element instanceof Engine) {
				Engine engine = (Engine) element;
				engine.print("Constructing Engine");
			}
		}for (CarElement element : car.getElements()) {
			if (element instanceof Wheel) {
				Wheel wheel = (Wheel) element;
				wheel.print("Printing left");
			}if (element instanceof Body) {
				Body body = (Body) element;
				body.print("Printing Body");
			}if (element instanceof Engine) {
				Engine engine = (Engine) element;
				engine.print("Printing Engine");
			}
		}
	}
}
