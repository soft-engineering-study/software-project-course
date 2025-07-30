package br.ic.ufal.employees;

public abstract class Employee
{
    
    private String name; 
    
    protected String address; 
    
    double timeCard; 

    public Employee(){}

    public Employee(String name){
        this.name = name;
        
        
    }

    public Employee(String name, String address, double timeCard){
        this.name = name; 
        this.address = address;
        this.timeCard = timeCard; 
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public double getTimeCard() {
        return timeCard;
    }

    public void setTimeCard(double timeCard) {
        this.timeCard = timeCard;
    }

    public String printEmployeeInfo(){
        return "Name: " + this.name +
               "\nAddress: " + this.address +
               "\nTime Card: " + this.timeCard;
    }

    public String printEmployeeInfo(Employee employee){
        return "Name: " + this.name +
               "\nAddress: " + this.address +
               "\nTime Card: " + this.timeCard +
               "\n----------------------------" +
               "\nName: " + employee.name +
               "\nAddress: " + employee.address +
               "\nTime Card: " + employee.timeCard;
    }

    

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Name: " + this.name +
               "\nAddress: " + this.address +
               "\nTime Card: " + this.timeCard;
    }    
    
}




