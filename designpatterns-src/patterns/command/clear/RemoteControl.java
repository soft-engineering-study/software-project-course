package patterns.command.clear;

import java.util.*;

//
// This is the invoker
//
public class RemoteControl {
	Command slot;
 
	public RemoteControl() {}
 
	public void setCommand(Command command) {
		slot = command;
	}
 
	public void buttonWasPressed() {
		slot.execute();
	}
}
