import java.util.Properties;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import java.io.*;

/**
 * Runs queries against a back-end database
 * (CSE 344 homework 5, sample solution)
 */
public class Query {
	private String configFilename;
	private Properties configProps = new Properties();

	private String jSQLDriver;
	private String imdbUrl;
	private String customerUrl;
	private String jSQLUser;
	private String jSQLPassword;

	// DB Connections
	private Connection imdbConn;
	private Connection customerConn;

	// Canned queries

	// Fixed the SQL injection in search by using a ? parameter,
	// forcing us to change search to be a PreparedStatement
       /* kmorton: SQL Server automatically assumes case insensitivity with LIKE*/
	private static final String SEARCH_SQL = 
		"SELECT * FROM movie WHERE name LIKE ('%' + ? + '%') ORDER BY id";
	private PreparedStatement searchStatement;
	// Notes on the SQL used in SEARCH_SQL: 
	// (SQL Server uses + to concatenate; most other DBMSes are like Postgres with ||)
       

	private static final String DIRECTOR_MID_SQL = "SELECT y.* "
					 + "FROM movie_directors x, directors y "
					 + "WHERE x.mid = ? and x.did = y.id";
	private PreparedStatement directorMidStatement;

	/* uncomment, and edit, after your create your own customer database */
	private static final String CUSTOMER_LOGIN_SQL = 
		"SELECT * FROM customers WHERE login = ? and password = ?";
	private PreparedStatement customerLoginStatement;

	private static final String BEGIN_TRANSACTION_SQL = 
	    "BEGIN TRANSACTION;";
	    
	private PreparedStatement beginTransactionStatement;

	private static final String COMMIT_SQL = "COMMIT TRANSACTION;";
	private PreparedStatement commitTransactionStatement;

	private static final String ROLLBACK_SQL = "ROLLBACK TRANSACTION";
	private PreparedStatement rollbackTransactionStatement;
	
	/* additional queries */
	private static final String CUSTOMER_NAME_SQL = 
		"SELECT fname, lname FROM customers WHERE cid = ?";
	private PreparedStatement customerNameStatement;

	private static final String ACTOR_MID_SQL = 
		"SELECT y.* " + 
		"FROM casts x, actor y " + 
		"WHERE x.mid = ? and x.pid = y.id";
	private PreparedStatement actorMidStatement;

	private static final String WHO_RENTS_MOVIE_SQL = 
		"SELECT cid " +
		"FROM movierentals " + 
		"WHERE mid = ? AND status = 'open'";
	private PreparedStatement whoRentsMovieStatement;

	private static final String RENTALS_REMAINING_SQL = 
		"SELECT (" +
		"(SELECT p.max_movies FROM RentalPlans p WHERE p.pid = c.pid) - " +
		"(SELECT count(*) FROM MovieRentals r WHERE r.cid = c.cid AND r.status = 'open')) " +
		"FROM customers c WHERE c.cid = ?";
	private PreparedStatement rentalsRemainingStatement;

	private static final String VALID_PLAN_SQL = 
		"SELECT pid FROM rentalplans WHERE pid = ?";
	private PreparedStatement validPlanStatement;

	private static final String VALID_MOVIE_SQL = 
		"SELECT mid FROM movie WHERE mid = ?";
	private PreparedStatement validMovieStatement;	

	private static final String PLANS_LIST_SQL = "SELECT * FROM rentalplans";
	private PreparedStatement plansListStatement;

	private static final String UPDATE_PLAN_SQL = 
		"UPDATE customers " +
		"SET pid = ? " +
		"WHERE cid = ?";
	private PreparedStatement updatePlanStatement;

	private static final String RENT_SQL = 
		"INSERT INTO MovieRentals(mid, cid, date_out, status) " +
		"VALUES(?, ?, CURRENT_TIMESTAMP, 'open')";
	private PreparedStatement rentStatement;
	
	private static final String RETURN_SQL = 
		"UPDATE MovieRentals " +
		"SET status = 'closed' " +
		"WHERE cid = ? AND mid = ?";
		// This actually closes all rentals of this movie by this customer
		// no matter when the rental went out, but this is not a problem
		// because there should be only one open rental anyway.
	private PreparedStatement returnStatement;
	
	private static final String FAST1_SQL = 
		"SELECT id, name, year " +
		"FROM Movie " +
		"WHERE name LIKE ? " + 
		"ORDER BY id";
	private PreparedStatement fast1_statement;
	
	private static final String FAST2_SQL = 
		"SELECT md.mid, d.fname, d.lname " +
		"FROM Movie m, Movie_Directors md, Directors d " +
		"WHERE m.id = md.mid AND md.did = d.id AND m.name LIKE ? " +
		"ORDER BY md.mid";
	private PreparedStatement fast2_statement;

	private static final String FAST3_SQL = 
		"SELECT c.mid, a.fname, a.lname " +
		"FROM Movie m, Casts c, Actor a " +
		"WHERE m.id = c.mid AND c.pid = a.id AND m.name LIKE ? " +
		"ORDER BY c.mid";
	private PreparedStatement fast3_statement;
	

	public Query(String configFilename) {
		this.configFilename = configFilename;
	}

    /**********************************************************/
    /* Connections to the Database Server */

	public void openConnection() throws Exception {
		configProps.load(new FileInputStream(configFilename));

		jSQLDriver   = configProps.getProperty("videostore.jdbc_driver");
		imdbUrl            = configProps.getProperty("videostore.imdb_url");
		customerUrl        = configProps.getProperty("videostore.customer_url");
		jSQLUser     = configProps.getProperty("videostore.sqlazure_username");
		jSQLPassword = configProps.getProperty("videostore.sqlazure_password");


		/* load jdbc drivers */
		Class.forName(jSQLDriver).newInstance();

		/* open connections to the imdb database */
		imdbConn = DriverManager.getConnection(imdbUrl, // database
						       jSQLUser, // user
						       jSQLPassword); // password
		
       		imdbConn.setAutoCommit(true);
		imdbConn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
		
		customerConn = DriverManager.getConnection (customerUrl,
							    jSQLUser,
							    jSQLPassword
		);

		customerConn.setAutoCommit(true);
		customerConn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
	}

	public void closeConnection() throws Exception {
		imdbConn.close();
		customerConn.close();
	}

    /**********************************************************/
    /* prepare all the SQL statements in this method.
      "preparing" a statement is almost like compiling it.  Note
       that the parameters (with ?) are still not filled in */

	public void prepareStatements() throws Exception {
		validMovieStatement = imdbConn.prepareStatement(VALID_MOVIE_SQL);
		searchStatement = imdbConn.prepareStatement(SEARCH_SQL);
		directorMidStatement = imdbConn.prepareStatement(DIRECTOR_MID_SQL);
		actorMidStatement = imdbConn.prepareStatement(ACTOR_MID_SQL);	

		fast1_statement = imdbConn.prepareStatement(FAST1_SQL);
		fast2_statement = imdbConn.prepareStatement(FAST2_SQL);
		fast3_statement = imdbConn.prepareStatement(FAST3_SQL);

		beginTransactionStatement = customerConn.prepareStatement(BEGIN_TRANSACTION_SQL);
		commitTransactionStatement = customerConn.prepareStatement(COMMIT_SQL);
		rollbackTransactionStatement = customerConn.prepareStatement(ROLLBACK_SQL);
						
		customerLoginStatement = customerConn.prepareStatement(CUSTOMER_LOGIN_SQL);
		customerNameStatement = customerConn.prepareStatement(CUSTOMER_NAME_SQL);

		whoRentsMovieStatement = customerConn.prepareStatement(WHO_RENTS_MOVIE_SQL);
		rentalsRemainingStatement = customerConn.prepareStatement(RENTALS_REMAINING_SQL);
		
		plansListStatement = customerConn.prepareStatement(PLANS_LIST_SQL);
		updatePlanStatement = customerConn.prepareStatement(UPDATE_PLAN_SQL);
		validPlanStatement = customerConn.prepareStatement(VALID_PLAN_SQL);
		
		rentStatement = customerConn.prepareStatement(RENT_SQL);
		returnStatement = customerConn.prepareStatement(RETURN_SQL);
	}


    /**********************************************************/
    /* Suggested helper functions; you can complete these, or write your own
       (but remember to delete the ones you are not using!) */
	
	// Notice that even those helper functions that read or write the customer database
	// (and thus should be executed in a transaction on customer) do not use transactions
	// directly.  This is because the functions that call these helpers already use
	// transactions.  To use transactions inside the helper functions as well will 
	// cause transaction nesting, which Postgres does not support. SQL Azure does support nesting, however 

	public int getRemainingRentals(int cid) throws Exception {
		/* How many movies can she/he still rent?
		   You have to compute and return the difference between the customer's plan
		   and the count of outstanding rentals */
		rentalsRemainingStatement.clearParameters();
		rentalsRemainingStatement.setInt(1, cid);
		
		ResultSet rentalsLeftSet = rentalsRemainingStatement.executeQuery();
		rentalsLeftSet.next();
		int c = rentalsLeftSet.getInt(1);
		
		rentalsLeftSet.close();
		return c;
	}

	public String getCustomerName(int cid) throws Exception {
		/* Find the first and last name of the current customer. */
		customerNameStatement.clearParameters();
		customerNameStatement.setInt(1, cid);
		
		ResultSet nameSet = customerNameStatement.executeQuery();
		nameSet.next();
		String name = 
			nameSet.getString("fname") + " " +
			nameSet.getString("lname");
		nameSet.close();
		return name;
	}

	public boolean isValidPlan(int planid) throws Exception {
		/* Is planid a valid plan ID?  You have to figure it out */
		validPlanStatement.clearParameters();
		validPlanStatement.setInt(1, planid);
		ResultSet validSet = validPlanStatement.executeQuery();
		boolean valid = validSet.next();
		validSet.close();
		return valid;
	}

	public boolean isValidMovie(int mid) throws Exception {
		/* is mid a valid movie ID?  You have to figure it out */
		validMovieStatement.clearParameters();
		validMovieStatement.setInt(1, mid);
		ResultSet validSet = validMovieStatement.executeQuery();
		boolean valid = validSet.next();
		validSet.close();
		return valid;
	}

	private int getRenterID(int mid) throws Exception {
		/* Find the customer id (cid) of whoever currently rents the movie mid; return -1 if none */
		whoRentsMovieStatement.clearParameters();
		whoRentsMovieStatement.setInt(1, mid);
		
		ResultSet rentsSet = whoRentsMovieStatement.executeQuery();
		int cid;
		if (rentsSet.next()) {
			cid = rentsSet.getInt("cid");
		} else {
			cid = -1;
		}
		rentsSet.close();
		return cid;
	}


	
    /**********************************************************/
    /* login transaction: invoked only once, when the app is started  */
	public int transaction_login(String name, String password) throws Exception {
		/* authenticates the user, and returns the user id, or -1 if authentication fails */

		/* Uncomment after you create your own customers database */
		int cid;

		customerLoginStatement.clearParameters();
		customerLoginStatement.setString(1,name);
		customerLoginStatement.setString(2,password);
	    ResultSet cid_set = customerLoginStatement.executeQuery();
	    if (cid_set.next()) cid = cid_set.getInt(1);
		else cid = -1;
		return(cid);
		// N.B.: It's ok to omit SQL transactional context for this "transaction,"
		// because there is no way to change the username or password of a customer
		// from within our application.

	}

	public void transaction_printPersonalData(int cid) throws Exception {
		/* println the customer's personal data: name, and plan number */
		// (typo - we said plan number, we meant remaining rental count, as per web instructions)
		
		// Here, a database transaction is needed, because
		// the remaining rental count can be changed by rent, return,
		// and plan change actions.
		
	        beginTransaction();
		System.out.println("Welcome, " + getCustomerName(cid));
		System.out.println("You may rent " + getRemainingRentals(cid) + " more movies.");
		commitTransaction();
	}


    /**********************************************************/
    /* main functions in this project: */

	public void transaction_search(int cid, String movie_title)
			throws Exception {
		/* searches for movies with matching titles: SELECT * FROM movie WHERE name LIKE movie_title */
		/* prints the movies, directors, actors, and the availability status:
		   AVAILABLE, or UNAVAILABLE, or YOU CURRENTLY RENT IT */

		// It's a judgment call whether you should put this transaction into
		// a SQL transaction on customer, because it's not critical that you
		// show the most up to date availability information.
		//
		// We don't use a transaction here.
		//
		searchStatement.setString(1, movie_title);
		ResultSet movie_set = searchStatement.executeQuery();
		while (movie_set.next()) {
			int mid = movie_set.getInt(1);
			System.out.println("ID: " + mid + " NAME: "
					+ movie_set.getString(2) + " YEAR: "
					+ movie_set.getString(3));
			/* do a dependent join with directors */
			directorMidStatement.clearParameters();
			directorMidStatement.setInt(1, mid);
			ResultSet director_set = directorMidStatement.executeQuery();
			while (director_set.next()) {
				System.out.println("\t\tDirector: " + director_set.getString(3)
						+ " " + director_set.getString(2));
			}
			director_set.close();
			
			/* now you need to retrieve the actors, in the same manner */
			actorMidStatement.clearParameters();
			actorMidStatement.setInt(1, mid);
			ResultSet actor_set = actorMidStatement.executeQuery();
			while (actor_set.next()) {
				System.out.println("\t\tActor: "
						+ actor_set.getString("fname") + " "
						+ actor_set.getString("lname"));
			}
			actor_set.close();

			/* then you have to find the status: of "AVAILABLE" "YOU HAVE IT",
			 * "UNAVAILABLE" */
			int hasMovie = getRenterID(mid);
			if (hasMovie == -1)
				System.out.println("\t\tAVAILABLE");
			else if (hasMovie == cid)
				System.out.println("\t\tYOU HAVE IT");
			else
				System.out.println("\t\tUNAVAILABLE");
		}
		System.out.println();
	}

	public void transaction_choosePlan(int cid, int pid) throws Exception {
	    /* updates the customer's plan to pid: UPDATE customer SET plid = pid */

		beginTransaction();
		

		updatePlanStatement.clearParameters();
		updatePlanStatement.setInt(1, pid);
		updatePlanStatement.setInt(2, cid);
		updatePlanStatement.executeUpdate();
		
		// rollback if customer has too many movies 	
		int remaining = getRemainingRentals(cid);
		
		if (remaining < 0) {
			rollbackTransaction();
			System.out.println("You cannot switch to this plan unless you return some movies.");
		} else {
			commitTransaction();
		}
	}

	public void transaction_listPlans() throws Exception {
	    /* println all available plans: SELECT * FROM plan */
		ResultSet plansSet = plansListStatement.executeQuery();
		while (plansSet.next()) {
			System.out.printf (
				"%d\t%-20s\tmax %d movies\t$%.2f", 
				plansSet.getInt("pid"), 
				plansSet.getString("name"),
				plansSet.getInt("max_movies"), 
				plansSet.getDouble("fee")
			);
			System.out.println();
		}
		plansSet.close();
	}

	public void transaction_rent(int cid, int mid) throws Exception {
	    /* rent the movie mid to the customer cid */
		beginTransaction();
		
		
		int remaining = getRemainingRentals(cid);
		if (remaining <= 0) {
			rollbackTransaction();
			System.out.println("You cannot rent more movies with your current plan.");
			return;
		}
		
		int hasMovie = getRenterID(mid);
		// pause for debugging
		(new BufferedReader(new InputStreamReader(System.in))).readLine();
		
		if (hasMovie == -1) {
			rentStatement.clearParameters();
			rentStatement.setInt(1, mid);
			rentStatement.setInt(2, cid);
			rentStatement.executeUpdate();
			commitTransaction();
			return;
		}
		
		
		rollbackTransaction();
		if (hasMovie == cid) {
			System.out.println("You already rented this movie.");
		} else {
			System.out.println("Somebody else is already renting this movie.");
		}
	}

	public void transaction_return(int cid, int mid) throws Exception {
	    /* return the movie mid by the customer cid */
		beginTransaction();
		
		
		int hasMovie = getRenterID(mid);

		// pause for debugging
		(new BufferedReader(new InputStreamReader(System.in))).readLine();

		if (hasMovie == cid) {
			returnStatement.clearParameters();
			returnStatement.setInt(1, cid);
			returnStatement.setInt(2, mid);
			returnStatement.executeUpdate();
			commitTransaction();
			return;
		}
		
		rollbackTransaction();		
		System.out.println("You are not currently renting this movie.");		
	}

	public void transaction_fastSearch(int cid, String movie_title)
			throws Exception {
		/* like transaction_search, but uses joins instead of dependent joins
		   Needs to run three SQL queries: (a) movies, (b) movies join directors, (c) movies join actors
		   Answers are sorted by mid.
		   Then merge-joins the three answer sets */
		
		fast1_statement.clearParameters();
		fast1_statement.setString(1, '%' + movie_title + '%');
		ResultSet rs1 = fast1_statement.executeQuery();
		
		fast2_statement.clearParameters();
		fast2_statement.setString(1, '%' + movie_title + '%');
		ResultSet rs2 = fast2_statement.executeQuery();
		
		fast3_statement.clearParameters();
		fast3_statement.setString(1, '%' + movie_title + '%');
		ResultSet rs3 = fast3_statement.executeQuery();
		
		boolean rs2more = rs2.next();
		boolean rs3more = rs3.next();
		
		while (rs1.next())
		{
			int mid = rs1.getInt(1);
			System.out.println("ID: " + mid + " NAME: "
					+ rs1.getString(2) + " YEAR: "
					+ rs1.getString(3));
			
			while (rs2more && rs2.getInt(1) < mid)
				rs2more = rs2.next();			
			while (rs2more && rs2.getInt(1) == mid)
			{
				System.out.println("\t\tDirector: " + rs2.getString(2)
						+ " " + rs2.getString(3));
				rs2more = rs2.next();
			}
			
			while (rs3more && rs3.getInt(1) < mid)
				rs3more = rs3.next();			
			while (rs3more && rs3.getInt(1) == mid)
			{
				System.out.println("\t\tActor: " + rs3.getString(2)
						+ " " + rs3.getString(3));
				rs3more = rs3.next();
			}
		}
		rs1.close();
		rs2.close();
		rs3.close();
	}

        public void beginTransaction() throws Exception {
	    customerConn.setAutoCommit(false);
	    beginTransactionStatement.executeUpdate();
	}

        public void commitTransaction() throws Exception {
	    commitTransactionStatement.executeUpdate();
	    customerConn.setAutoCommit(true);
	}
        public void rollbackTransaction() throws Exception {
	    rollbackTransactionStatement.executeUpdate();
	    customerConn.setAutoCommit(true);
        }
	
}
