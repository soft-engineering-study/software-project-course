package patterns.command.smells;
public class RemoteControl {

	private GarageDoor garageDoor = new GarageDoor();
	private Light light = new Light();
	
	public RemoteControl() {
		
	}
	
	public void execute(Command command) {
		
		if (command.equals(Command.UP)) {
			garageDoor.up();
		} if (command.equals(Command.DOWN)) {
			garageDoor.down();
		} if (command.equals(Command.GARAGE_LIGHT_ON)) {
			garageDoor.lightOn();
		} if (command.equals(Command.GARAGE_LIGHT_OFF)) {
			garageDoor.lightOff();
		} if (command.equals(Command.ON)) {
			light.on();
		} if (command.equals(Command.OFF)) {
			light.off();
		}
	}
	
}
