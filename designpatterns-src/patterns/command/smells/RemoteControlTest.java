package patterns.command.smells;
public class RemoteControlTest {
	public static void main(String[] args) {
		
		RemoteControl remoteControl = new RemoteControl();
		
		remoteControl.execute(Command.UP);
		
    }
}
