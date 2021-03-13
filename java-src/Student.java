package java;
public class Student {

    private String name;
    private double average;

    public Student(String name, double average) {
        this.name = name;

        // validate that average is > 0.0 and <= 100.0; otherwise, keep instance variable average's default value (0,0)
        if (average  > 0.0)
            if (average <= 100.0)
                this.average = average;
    }

    // Sets the student's name
    public void setName(String name) {
        this.name = name;
    }

    // retrieves the student's name
    public String getName() {
        return name;
    }

    // sets the student's average
    public void setAverage(double average) {
        // validate that average is > 0.0 and <= 100.0; otherwise, keep instance variable average's current value
        if (average > 0.0)
            if (average <= 100.0)
                this.average = average;
    }

    // retrieves the student's average
    public double getAverage() {
        return average;
    }

    public String getLetterGrade() {
        String letterGrade = "";

        if (average >= 90.0)
            letterGrade = "A";
        else if (average >= 80.0)
            letterGrade = "B";
        else if (average >= 70.0)
            letterGrade = "C";
        else if (average >= 60.0)
            letterGrade = "D";
        else
            letterGrade = "F";

        return letterGrade;
    }

}
