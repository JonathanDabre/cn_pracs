import java.io.*;
import java.net.*;

public class JonServer{

    public static void main(String[] args) {
        try {

            // We will create server socket that listens to specified port in the argument
            ServerSocket ss = new ServerSocket(6666);
            // ss accepts incoming client connection from port 6666

            //As soon as client connection is accepted(recieved) by ss we create socket s to communicate with client.
            Socket s = ss.accept();

            //DataInputStream to read data from input stream in binary, utf encoding, primitive datatypes etc.
            DataInputStream dis = new DataInputStream(s.getInputStream());

            //Message converted to str
            String str = (String) dis.readUTF();

            System.out.println("Message: " + str);

            //release the resources after use by...
            ss.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}