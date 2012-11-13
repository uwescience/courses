import java.sql.*;
import java.util.*;

class Section7_T1 {
	static final int UPDATE_VALUE = 11;
	static Connection conn;

	public static void main (String[] args) throws Exception {
		Class.forName("org.postgresql.Driver");
		conn = DriverManager.getConnection (
			"jdbc:postgresql:cse344", // change this to your DB name
			"michaelr",
			"ignored"
		);
		
		System.out.println("Running T1()");
		Section7Conflicting t1 = new Section7Conflicting(conn, 1, UPDATE_VALUE);
		// Uncomment one of the lines below to try each scenario
		//t1.badTransaction();
		//t1.rolledBack();
		//t1.retryUntilSuccess();
		System.out.println();
	}
}
