package patterns.introducenullobjects.clear;

public class NavigationApplet extends Applet {

	private MouseEventHandler mouseEventHandler = new NullMouseEventHandler();
	
	public NavigationApplet(MouseEventHandler mouseEventHandler) {
		// TODO Auto-generated constructor stub
		this.mouseEventHandler = mouseEventHandler;
	}
	
	@Override
	public boolean mouseMove() {
		// TODO Auto-generated method stub
		return mouseEventHandler.mouseMove();
	}

	@Override
	public boolean mouseDown() {
		// TODO Auto-generated method stub
		
		return mouseEventHandler.mouseDown();
	}

	@Override
	public boolean mouseUp() {
		// TODO Auto-generated method stub
		return mouseEventHandler.mouseUp();
	}

	@Override
	public boolean mouseExit() {
		// TODO Auto-generated method stub
		return mouseEventHandler.mouseExit();
	}
}
