package patterns.extractclass.smells;

public class Company {

	private String cnpj;
	private String areaCode;
	private String number;
	
	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	
	public String getCnpj() {
		return cnpj;
	}
	
	public String getTelephoneNumber(){
		return this.areaCode + this.number;
	}
}
