package Introduction;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.*;

public class EndOfFile {

    public static void main(String[] args){

        //Using Scanner
        try {

            Scanner myObj = new Scanner(new File("src/Introduction/input.txt"));//System.in

            System.out.println("Scanner:");

            Integer lineNum = 1;
            while (myObj.hasNextLine()) {
                String line = myObj.nextLine();
                System.out.println(lineNum.toString() +  " " + line);
                lineNum++;
            }

        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        }


        System.out.println();
        System.out.println("Streams:");
        //Using Streams
        try {
            Stream<String> stream = Files.lines(Paths.get("src/Introduction/input.txt"));

            stream.forEach(System.out::println);

            stream.close();

        } catch (IOException ex){
            ex.printStackTrace();
        }

    }

}
