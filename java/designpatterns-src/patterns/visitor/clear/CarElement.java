package patterns.visitor.clear;

interface CarElement {
	void accept(CarElementVisitor visitor); // CarElements have to provide accept().
}
