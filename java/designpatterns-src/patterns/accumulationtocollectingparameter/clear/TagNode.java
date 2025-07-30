package patterns.accumulationtocollectingparameter.clear;

import java.util.Iterator;

public class TagNode {
	
	private String tagName = null;
	private String attributes = null;
	private String tagValue = null;
	private String result = null;
	
	private String appendContentsTo( ){
		return writeOpenTagTo( ) + writeChildrenTo( ) + 
			   writeValueTo( ) + writeEndTagTo( ); }
	private String writeOpenTagTo( ) {
		return  result+="<" + tagName + " " + attributes + ">"; }
	private String writeChildrenTo( ){
		Iterator it = null;
		while(it.hasNext()){
		   TagNode node = (TagNode)it.next();
		   result += node.toString();
		} return result; }
	private String writeValueTo( ){
		 result += "<" + tagName + " " + attributes + ">";
		 if(! tagValue.equals(" "))
			   result+= tagValue;
		 return result; }
	private String writeEndTagTo( ){
		return result+= "<" + tagName + ">"; }
	public String toString() {
		return appendContentsTo( ); }
}
