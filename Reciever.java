import java.io.*;
import java.net.*;

public class Reciever {
  public static void main(String argv[]) throws Exception {
     ServerSocket hi;
     Socket client;
     BufferedReader br;
     DataOutputStream dos;

     String line;

     hi = new ServerSocket(5000);
     System.out.println("Server Listening on port 5000....");
     client = hi.accept();
     br = new BufferedReader(new InputStreamReader(client.getInputStream()));
     dos = new DataOutputStream(client.getOutputStream());
     while((line = br.readLine()) != null){
	System.out.println(line);
     }
  }
}
