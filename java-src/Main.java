import br.ic.ufal.entities.Employee;
import br.ic.ufal.entities.Hourly;
import br.ic.ufal.entities.Salaried;

public class Main {
    public static void main(String[] args) {

        Employee[] employees = new Employee[3];

        employees[0] = new Employee("Roberto");
        employees[1] = new Hourly("Bruno", 30);
        employees[2] = new Salaried("Jose", 1000);

        for (Employee employee : employees) {
            System.out.println(employee);
        }

        // Employee[] employees = new Employee[3];

        // employees[0] = new Employee();

        // employees[1] = new Hourly();

        // employees[2] = new Salaried();

        // employees[3] = new Commissioned();

        // Hourly h = new Employee();

        // Employee employee1 = new Employee("Prof. Baldoino", "Maceió", 7);

        // employee1.setTimeCard(-12);

        // System.out.println("Time Card: " + employee1.getTimeCard());

        // System.out.println(employee1.printEmployeeInfo());

        // System.out.println("===========================");

        // Employee employee2 = new Employee("Prof. Marcus", "Maceió", 8);

        // System.out.println(employee1.printEmployeeInfo(employee2));
    }
}

