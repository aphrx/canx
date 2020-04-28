
import java.io.*;
import java.net.*;

public class Sender {
   public static void main(String argv[]) throws Exception {
     Socket echo;
     BufferedReader br;
     String str;
     DataOutputStream dos;
     BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

     echo = new Socket("127.0.0.1", 5000);
     br = new BufferedReader(new InputStreamReader(echo.getInputStream()));
     dos = new DataOutputStream(echo.getOutputStream());
     while(str = br.readLine()){

	     System.out.println("I got: "+str);
	}
   }
}
