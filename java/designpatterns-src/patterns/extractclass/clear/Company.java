package patterns.extractclass.clear;

public class Company {

	private String cnpj;
	private Telephone telephone;
	
	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}
	
	public String getCnpj() {
		return cnpj;
	}
	
	public String getTelephoneNumber(){
		return this.telephone.getAreaCode() + this.telephone.getNumber();
	}
}
