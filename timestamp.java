package stopwatch;

import java.io.*;

public class timestamp implements Serializable {
    
    public int hrs;
    public int min;
    public int sec;
    public int milisec;
    public String name;

    public timestamp(int hrs, int min, int sec, int milisec,String newname) {
        this.hrs = hrs;
        this.min = min;
        this.sec = sec;
        this.milisec = milisec;
        this.name = newname;
    }
        
}
