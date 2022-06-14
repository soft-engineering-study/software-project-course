package  patterns.command.clear;

public class RemoteControlTest  {
	
	public static void main(String[] args) {
		RemoteControl remote = new RemoteControl();

		Light light = new Light();
		GarageDoor garageDoor = new GarageDoor();
		
		LightOnCommand lightOn = new LightOnCommand(light);
		GarageDoorOpenCommand garageOpen = new GarageDoorOpenCommand(garageDoor);
 
		remote.setCommand(lightOn);
		remote.buttonWasPressed();
		remote.setCommand(garageOpen);
		remote.buttonWasPressed();
    }
}
