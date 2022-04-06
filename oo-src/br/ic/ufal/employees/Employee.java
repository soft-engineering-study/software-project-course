package br.ic.ufal.employees;

import java.util.ArrayList;

public  class Employee
{
    public String name; 

    public Employee(){}

    public Employee(String name){
        this.name = name;
    }
   
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Name: " + this.name + "\n";
    }

    
}




