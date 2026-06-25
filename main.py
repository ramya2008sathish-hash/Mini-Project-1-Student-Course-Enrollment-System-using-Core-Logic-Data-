import java.util.ArrayList; 
import java.util.Scanner; 
 
class Student {     String name; 
    String course; 
 
    Student(String name, String course) {         this.name = name; 
        this.course = course; 
    } 
 
    public String toString() { 
        return name + " enrolled in " + course; 
    } 
} 
 
public class Main { 
 
    public static void main(String[] args) { 
 
        ArrayList<Student> students = new ArrayList<>(); 
        Scanner sc = new Scanner(System.in); 
 
        while (true) { 
            System.out.println("\n1. Add Student"); 
            System.out.println("2. Display Students"); 
            System.out.println("3. Search Student"); 
            System.out.println("4. Exit"); 
 
            System.out.print("Enter choice: ");             int choice = sc.nextInt(); 
            sc.nextLine(); 
 
            switch (choice) { 
                 case 1: 
                    System.out.print("Enter Name: "); 
                    String name = sc.nextLine(); 
 
                    System.out.print("Enter Course: "); 
                    String course = sc.nextLine(); 
 
                    students.add(new Student(name, course));                     System.out.println("Student Added!");                     break; 
                 case 2: 
                    System.out.println("\nEnrolled Students:"); 
                    for (Student s : students) { 
                        System.out.println(s); 
                    }                     break; 
                 case 3: 
                    System.out.print("Enter name to search: ");                     String search = sc.nextLine(); 
                    boolean found = false; 
 
                    for (Student s : students) {                         if (s.name.equalsIgnoreCase(search)) {                             System.out.println("Found: " + s); 
                            found = true; 
                        } 
                    } 
 
                    if (!found) { 
                        System.out.println("Student not found!"); 
                    }                     break; 
                 case 4: 
                    System.out.println("Exiting..."); 
                    return; 
                 default: 
                    System.out.println("Invalid choice!"); 
            } 
        } 
    } 
} 
