package patterns.introducenullobjects.clear;

public class NullMouseEventHandler implements MouseEventHandler{

	@Override
	public boolean mouseMove(){

		System.out.println("O objeto esta NULL");


		return true;
	}
	
	@Override
	public boolean mouseDown(){

		System.out.println("O objeto esta NULL");

		return true;
	}
	
	@Override
	public boolean mouseUp(){
		return true;
	}
	
	@Override
	public boolean mouseExit(){
		return true;
	}
}
