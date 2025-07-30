import java.util.ArrayList;

import br.ic.ufal.employees.Commissioned;
import br.ic.ufal.employees.Employee;
import br.ic.ufal.employees.Hourly;
import br.ic.ufal.employees.Salaried;


public class Main {
    public static void main(String[] args) {
         
        Box<Employee> eBox = new Box<Employee>();
 
        
        ArrayList<Employee> employees = new ArrayList<>();
        
        employees.add(new Hourly("Bruno", "UFAL", 16, 4));
        employees.add(new Salaried("Marcelo", "Reitoria", 15, 8));
        employees.add(new Commissioned("João", "IC", 12, 200));


        for (Employee employee : employees) {

            if(employee instanceof Hourly){
                Hourly hourly = (Hourly)employee;
                System.out.println(hourly.getWorkingHours());
            } else{
                System.out.println(employee);
                System.out.println("========================");
            }
            
            
            
            
        }
    }
}

