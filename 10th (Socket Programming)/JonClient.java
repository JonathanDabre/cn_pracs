import java.io.*;
import java.net.*;

public class JonClient {
    public static void main(String[] args) {
        try {

            // we create socket that makes client run (make connection) on port 6666
            Socket s = new Socket("localhost", 6666);

            // DataOutputStream to send data from output stream in a particular type(binary/utf/string).
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            //Convert string to utf, to send using dout.
            dout.writeUTF("Hello Server, I'm Funtend, messaging from client side.");
            dout.flush(); //send any pending data immediately
            dout.close(); 

            s.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
