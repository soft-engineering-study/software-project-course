package patterns.introducenullobjects.smells;

public class NavigationApplet extends Applet {

	private MouseEventHandler mouseEventHandler = null;
	
	public NavigationApplet(MouseEventHandler mouseEventHandler) {
		// TODO Auto-generated constructor stub
		this.mouseEventHandler = mouseEventHandler;
	}
	
	@Override
	public boolean mouseMove() {
		// TODO Auto-generated method stub
		if (mouseEventHandler != null) {
			mouseEventHandler.mouseMove();
		}
		
		return true;
	}

	@Override
	public boolean mouseDown() {
		// TODO Auto-generated method stub
		
		if (mouseEventHandler != null) {
			mouseEventHandler.mouseDown();
		}
		
		return true;
	}

	@Override
	public boolean mouseUp() {
		// TODO Auto-generated method stub
		if (mouseEventHandler != null) {
			mouseEventHandler.mouseUp();
		}
		return true;
	}

	@Override
	public boolean mouseExit() {
		// TODO Auto-generated method stub
		if (mouseEventHandler != null) {
			mouseEventHandler.mouseExit();
		}
		return true;
	}

}
