import java.sql.*;
import java.util.*;

class Section7 {
	static Connection conn;

	public static void main (String[] args) throws Exception {
		Class.forName("org.postgresql.Driver");
		conn = DriverManager.getConnection (
			"jdbc:postgresql:cse344", // change this to your DB name
			"michaelr",
			"ignored"
		);
		
		System.out.println("Running sqlTxCode()");
		sqlTxCode();
		System.out.println();

		System.out.println("Running javaTxCode()");
		javaTxCode();
		System.out.println();
	}
	
	static void sqlTxCode() throws SQLException {
		Statement stmt = conn.createStatement();
		stmt.executeUpdate(
			"BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE");
		
		ResultSet results = stmt.executeQuery("select * from R");
		while (results.next()) {
			System.out.printf("a=%d, b=%d", 
				results.getInt("a"), results.getInt("b"));
			System.out.println();
		}
		results.close();
		
		stmt.executeUpdate("COMMIT");
	}
	
	static void javaTxCode() throws SQLException {
		// force everything to be in a transaction
		conn.setAutoCommit(false);
		
		Statement stmt = conn.createStatement();
		ResultSet results = stmt.executeQuery("select * from R");
		while (results.next()) {
			System.out.printf("a=%d, b=%d", 
				results.getInt("a"), results.getInt("b"));
			System.out.println();
		}
		results.close();
		
		conn.commit();
		// now each SQL statement executes separately again
		conn.setAutoCommit(true);
	}
}
