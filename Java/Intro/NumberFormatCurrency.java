import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class NumberFormatCurrency {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        // Write your code here.
        //NumberFormat nf = NumberFormat.getInstance();
        Locale indiaLocale = new Locale("en", "IN");//Custom Locale
        NumberFormat unf = NumberFormat.getCurrencyInstance(Locale.US);
        String us = unf.format(payment);
        NumberFormat inf = NumberFormat.getCurrencyInstance(indiaLocale);
        String india = inf.format(payment);
        NumberFormat cnf = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = cnf.format(payment);
        NumberFormat fnf = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = fnf.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
