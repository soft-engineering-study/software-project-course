package patterns.introducenullobjects.clear;

public class NullMouseEventHandler implements MouseEventHandler{

	@Override
	public boolean mouseMove(){
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
