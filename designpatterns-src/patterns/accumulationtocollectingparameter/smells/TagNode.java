package patterns.accumulationtocollectingparameter.smells;

import java.util.Iterator;

public class TagNode {
	@Override
	public String toString() {
		String tagName = null;
		String attributes = null;
		String tagValue = null;
		
		String result = new String();
		result += "<" + tagName + " " + attributes + ">";
		Iterator it = null;
		while(it.hasNext()){
		   TagNode node = (TagNode)it.next();
		   result += node.toString();
		}
		if(! tagValue.equals(" "))
		   result+= tagValue;
		result+= "<" + tagName + ">";
		return result;
	}
}
