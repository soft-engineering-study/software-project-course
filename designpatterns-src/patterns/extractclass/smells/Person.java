package patterns.extractclass.smells;

public class Person {

	private String name;
	private String areaCode;
	private String number;
	
	public void setName(String name) {
		this.name = name;
	} 
	
	public String getName() {
		return name;
	}
	
	public String getTelephoneNumber(){
		return this.areaCode + this.number;
	}
}
