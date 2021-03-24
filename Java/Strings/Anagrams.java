import java.util.Scanner;

public class Anagrams {

    static boolean isAnagram(String a, String b) {
        StringBuilder aa = new StringBuilder(a.toLowerCase());
        StringBuilder bb = new StringBuilder(b.toLowerCase());

        if (aa.length() != bb.length()) {
            return false;
        } else {
            for (int i=0; i < aa.length(); i++){
                for(int j=0; j < bb.length(); j++){
                    if(aa.charAt(i) == bb.charAt(j)) {
                        bb.deleteCharAt(j);
                        break;
                    }
                }

            }
        }
        if(bb.length() == 0) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
