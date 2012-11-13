import java.sql.*;
import java.util.*;

class Section7Conflicting {
	Connection conn;
	int txId, updateValue;

	public Section7Conflicting(Connection conn, int transactionId,
		int updateValue) {
		this.conn = conn;
		this.txId = transactionId;
		this.updateValue = updateValue;
	}
	
	void badTransaction() throws SQLException {
		Statement stmt = conn.createStatement();
		stmt.executeUpdate(
			"begin transaction isolation level serializable");
		
		ResultSet results = stmt.executeQuery("select * from R");
		results.close();
		
		PreparedStatement pstmt = conn.prepareStatement(
			"update r set b= ? where a=1");
		pstmt.setInt(1, updateValue);
		pstmt.executeUpdate();
		
		// pause for debugging
		Scanner stdin = new Scanner(System.in);
		stdin.nextLine();
		
		stmt.executeUpdate("commit");
	}
	
	void rolledBack() throws SQLException {
		try {
			badTransaction();
		} catch (SQLException ex) {
			conn.createStatement().executeUpdate("rollback");
			System.out.println("Caught a Postgres error:");
			ex.printStackTrace();
		}
	}
	
	void retryUntilSuccess() throws SQLException {
		int attemptCount = 1;
		outer: while (true) {
			System.out.println("Attempt " + attemptCount);
			try {
				badTransaction();
				break outer;
			} catch (SQLException ex) {
				conn.createStatement().executeUpdate("rollback");
				System.out.println("...failed with this Postgres error:");
				ex.printStackTrace();
				attemptCount++;
			}
		}
	}
}
