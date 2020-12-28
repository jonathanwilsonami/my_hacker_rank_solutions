import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaStaticInitializerBlock {
    static Scanner myObj = new Scanner(System.in);
    static int B = myObj.nextInt();
    static int H = myObj.nextInt();
    static boolean flag = true;
    
    static {
        try {
            if (B <= 0 || H <= 0 ) 
                throw new Exception ("Breadth and height must be positive");
        } catch (java.lang.Exception ex) {
            flag = false;
            System.out.println(ex);
        }
            
    }

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class
