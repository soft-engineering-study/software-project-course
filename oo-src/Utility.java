import java.util.ArrayList;

import br.ic.ufal.employees.Employee;

public class Utility<E> {

    public Utility(){

       
        
    }
    
    public void printArray(E[] elements){
        for (E element : elements) {
            System.out.println(element);
        }
    }
}
