package patterns.visitor.smells;

public class Car {

	private CarElement[] elements;
	 
    public Car() {
        //create new Array of elements
        this.elements = new CarElement[] { new Wheel( ), 
            new Wheel( ), new Wheel( ) , 
            new Wheel( ), new Body(), new Engine() };
    }
    
    public CarElement[] getElements() {
		return elements;
	}
}
