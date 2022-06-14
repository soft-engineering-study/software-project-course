package patterns.introducenullobjects.clear;

public class MouseEventHandlerStandard implements MouseEventHandler{

	@Override
	public boolean mouseMove(){

		System.out.println("Mouse is moving");

		return true;


	}
	
	@Override
	public boolean mouseDown(){
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
