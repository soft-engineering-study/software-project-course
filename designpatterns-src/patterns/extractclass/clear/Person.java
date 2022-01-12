package patterns.extractclass.clear;

public class Person {

	private String name;
	private Telephone telephone = new Telephone();

	public void setName(String name) {
		this.name = name;
	} 
	
	public String getName() {
		return name;
	}
	
	public String getTelephoneNumber(){
		return this.telephone.getAreaCode() + this.telephone.getNumber();
	}
}
