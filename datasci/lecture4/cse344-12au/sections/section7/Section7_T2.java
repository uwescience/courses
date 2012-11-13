import java.sql.*;
import java.util.*;

class Section7_T2 {
	static final int UPDATE_VALUE = 12;
	static Connection conn;

	public static void main (String[] args) throws Exception {
		Class.forName("org.postgresql.Driver");
		conn = DriverManager.getConnection (
			"jdbc:postgresql:cse344", // change this to your DB name
			"michaelr",
			"ignored"
		);
		
		System.out.println("Running T2()");
		Section7Conflicting t2 = new Section7Conflicting(conn, 2, UPDATE_VALUE);
		// Uncomment one of the lines below to try each scenario
		//t2.badTransaction();
		//t2.rolledBack();
		//t2.retryUntilSuccess();
		System.out.println();
	}
}
