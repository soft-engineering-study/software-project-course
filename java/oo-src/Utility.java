import java.util.ArrayList;

import br.ic.ufal.employees.Employee;

public class Utility<E> {

    public Utility(){

       Employee employee = new Employee();
        
    }
    
    public void printArray(E[] elements){
        for (E element : elements) {
            System.out.println(element);
        }
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString();
    }
}
