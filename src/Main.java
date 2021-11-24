import java.util.ArrayList;
import java.util.List;

import br.ic.ufal.employees.Commissioned;
import br.ic.ufal.employees.Employee;
import br.ic.ufal.employees.Hourly;
import br.ic.ufal.employees.Salaried;

public class Main {
    public static void main(String[] args) {
     

        List<Hourly> employees = new ArrayList<Hourly>();

        /*ArrayList<Hourly> employees = new ArrayList<Hourly>();

        employees.add(new Hourly("Bruno", 30));
        //employees.add(new Salaried("Jose", 1000));
        //employees.add(new Commissioned("Rangel", 1000));

        
        for (Employee employee : employees) {
            System.out.println("//================");
            System.out.println(employee);

            ((Hourly)employee).getWorkingHours();
        }*/

       

        

        

        /*ArrayList<Employee> employees = new ArrayList<Employee>();

        employees.add(new Employee("Roberto")); 
        employees.add(new Hourly("Bruno", 30));
        employees.add(new Salaried("Jose", 1000));
        employees.add(new Commissioned("Rangel", 1000));

        for (Employee employee : employees) {
            System.out.println("//================");
            System.out.println(employee);
        }

         /*System.out.println("//-------------------- Hourly ------");
        Employee employee = new Hourly("Paloma", 60);

        System.out.println(employee);

        System.out.println("//-------------------- Comissioned -----");

        employee = new Commissioned("Rangel", 1000);

        System.out.println(employee);

        System.out.println("//-------------------- Salaried -----");

        employee = new Salaried("Ewerton", 20000);
        System.out.println(employee);*/

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

