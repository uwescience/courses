import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class VideoStore {
	private static final String DBCONFIG_FILENAME = "dbconn.properties";

	public static void usage() {
		/* prints the choices for commands and parameters */
		System.out.println();
		System.out.println(" *** Please enter one of the following commands *** ");
		System.out.println("> search <movie title>");
		System.out.println("> plan [<plan id>]");
		System.out.println("> rent <movie id>");
		System.out.println("> return <movie id>");
		System.out.println("> fastsearch <movie title>");
		System.out.println("> quit");
	}

	public static void menu(int cid, Query q) throws Exception {
		/* cid = customer id (obtained from the command line) */

		/* prepare to read the user's command and parameter(s) */
		String response = null;

		while (true) {
			usage();

			BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
			/* before prompting the user, tell her/him how many movies he can still rent */
			q.transaction_printPersonalData(cid);
			System.out.print("> ");

			response = r.readLine();
			if (response.trim().length() == 0) {
				System.out.println("Sorry, please give a command");
				continue; // back to top of loop
			}

			StringTokenizer st = new StringTokenizer(response);
			String t = st.nextToken();

			if (t.equals("search")) {
				/* search for a movie whose title matches a string */
				if (st.hasMoreTokens()) {
					String movie_title = st.nextToken("\n").trim(); /* read the rest of the line */
					System.out.println("Searching for the movie '"
									   + movie_title + "'");
					q.transaction_search(cid, movie_title);
				} else {
					System.out.println("Error: need to type in movie title");
				}
			}
			else if (t.equals("plan")) {
				/* choose a new rental plan, or, if none is given, then list all available plans */
				if (st.hasMoreTokens()) {
					int plan_id = Integer.parseInt(st.nextToken());
					/* need to check that plan_id is a valid plan id in the database, */
					/* if yes, then set the new plan for the current customer */
					/* if not, then list all available plans */
					boolean correct_plan = q.isValidPlan(plan_id);
					if (correct_plan) {
						System.out.println("Switching to plan " + plan_id);
						q.transaction_choosePlan(cid, plan_id);
					} else {
						System.out.println("Incorrect plan id " + plan_id);
						System.out.println("Available plans are:");
						q.transaction_listPlans();
					}
				} else {
					System.out.println("Available plans:");
					q.transaction_listPlans();
				}
			}
			else if (t.equals("rent")) {
				/* rent the movie with the given movie id */
				int mid = Integer.parseInt(st.nextToken());
				System.out.println("Renting the movie id " + mid);
				q.transaction_rent(cid, mid);
			}
			else if (t.equals("return")) {
				/* return a movie previously rented */
				int mid = Integer.parseInt(st.nextToken());
				/* return the movie with mid */
				System.out.println("Returning the movie id " + mid);
				q.transaction_return(cid, mid);
			}
			else if (t.equals("fastsearch")) {
				/* same as search, only faster (and single words only) */
				if (st.hasMoreTokens()) {
					String movie_word = st.nextToken();
					System.out.println("Fast Searching for the movie '"
									   + movie_word + "'");
					q.transaction_fastSearch(cid, movie_word);
				} else {
					System.out
						.println("Error: need to type in movie title");
				}
			}
			else if (t.equals("quit")) {
				System.exit(0);
			}
			else {
				System.out.println("Error: unrecognized command '" + t
								   + "'");
			}
		}
	}

	public static void main(String[] args) throws Exception {
		if (args.length < 2) {
			System.out.println("Usage: java VideoStore CUSTOMER_ID CUSTOMER_PASSWORD");
			System.exit(1);
		}
		
		/* prepare the database connection stuff */
		Query q = new Query(DBCONFIG_FILENAME);
		q.openConnection();
		q.prepareStatements();

		/* authenticate the user */
		int cid = q.transaction_login(args[0], args[1]);			
		if (cid >= 0)
			menu(cid, q); /* menu(...) does the real work */
		else
			System.out.println("Sorry, login failed..."); /* innocent mistake, or malicious attack ? */
		q.closeConnection();
	}

}

