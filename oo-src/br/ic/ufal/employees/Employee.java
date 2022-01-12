package br.ic.ufal.employees;

import java.util.ArrayList;

public abstract  class Employee
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

    public abstract String definePayment(String paymentType);
    
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Name: " + this.name + "\n";
    }

    @Override
    public boolean equals(Object obj) {
        // TODO Auto-generated method stub
        return super.equals(obj);
    }
    
}




