import java.io.*;
import java.util.*;

public class PalindromeChecker {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
      
        //Long way
        char fromLeft;
        char fromRight;
        boolean palindrome = true;
        for(int i = 0; i < A.length(); i++){
            fromLeft = A.charAt(i);
            fromRight = A.charAt(A.length() - i - 1);
            if(fromLeft != fromRight){
                palindrome = false;
            }

        }
      
        if(palindrome) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        //Using reverse method from the StringBuilder
         System.out.println( A.equals( new StringBuilder(A).reverse().toString())
                ? "Yes" : "No" );
        
    }
}



