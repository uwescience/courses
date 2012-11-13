import java.util.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.io.*;

/**
 * Setup
 *
 * To run this example, you first need to create a table
 * in some database. Then, update the dbconn.properties
 * file to specify the driver, database, username, and password:
 * create table Account(id integer, value integer)
 * insert into Account values(0,100)
 * insert into Account values(1,100)
 */
public class TransactionsDemo {

    private static String configFilename = "dbconn.properties";
    private static Properties configProps = new Properties();

    private static String driver;
    private static String url;
    private static String user;
    private static String password;

    private static Connection db;

    private static final String read_sql = "select value from Account where id = 0";
    private static PreparedStatement read_statement;

    private static final String write_sql = "update Account set value = value + 100 where id = 0";
    private static PreparedStatement write_statement;

    private static final String count_sql = "select count(*) from Account";
    private static PreparedStatement count_statement;

    private static final String insert_sql = "insert into Account values(2,0)";
    private static PreparedStatement insert_statement;
   

    public static void main (String args[]) throws Exception {
 
        if (args.length < 1) {
            System.err.println ("Usage: java TransactionsDemo transactionNb");
            System.exit(1);
        } 

        int transactionNb = Integer.parseInt(args[0]);

        try {

            openConnection();
            prepareStatements();

            switch (transactionNb) {
            case 1: 
                runTransaction1();
                break;
            case 2:
                runTransaction2();
                break;
            case 3:
                runTransaction3();
                break;
            default:
                runTransaction4();
                break;
            }
        
            closeConnection();

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }


    public static void openConnection() throws Exception {

        configProps.load(new FileInputStream(configFilename));

        driver  = configProps.getProperty("driver");
        url = configProps.getProperty("url");
        user = configProps.getProperty("username");
        password = configProps.getProperty("password");

        Class.forName(driver).newInstance();

        db = DriverManager.getConnection(url, // database
                                         user, // user
                                         password); // password
		
        db.setAutoCommit(false);

    }

    public static void closeConnection() throws Exception {
        db.close();
    }

    public static void prepareStatements() throws Exception {
        read_statement = db.prepareStatement(read_sql);
        write_statement = db.prepareStatement(write_sql);
        count_statement = db.prepareStatement(count_sql);
        insert_statement = db.prepareStatement(insert_sql);
    }


    public static void readAccount() throws Exception {
        ResultSet value_set = read_statement.executeQuery();
        if (value_set.next()) {
            System.out.println("Value is " + value_set.getInt(1));
        }
    }

    public static void writeAccount() throws Exception {
        write_statement.executeUpdate();
    }

    public static void countAccounts() throws Exception {
        ResultSet value_set = count_statement.executeQuery();
        if (value_set.next()) {
            System.out.println("Value is " + value_set.getInt(1));
        }
    }

    public static void insertAccount() throws Exception {
        insert_statement.executeUpdate();
    }

    public static void runTransaction1() throws Exception {

        db.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
        //db.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);
  
        readAccount();
       
        Thread.sleep(5000);

        readAccount();
        
        db.commit();
    }

    public static void runTransaction2() throws Exception {

        db.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
        //db.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);  

        writeAccount();
        
        db.commit();

    }

    public static void runTransaction3() throws Exception {

        db.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);
        //db.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
  
        countAccounts();

        Thread.sleep(5000);

        countAccounts();
        
        db.commit();
    }

    public static void runTransaction4() throws Exception {

        db.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);
        //db.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);  

        insertAccount();

        db.commit();

    }

}
