Important: PostgreSQL users multiversion concurrency control.
For this reason, the anomalies that we are testing in this demo do not
show-up. There are lots of tricks with PostgreSQL isolation.
Best to check their documentation.

All works as expected with SQL Server because it users strict 2PL
for the standard levels of isolation.

To connect to postgres, use own local username and passwd.

For SQL Server, best to run this with SQLAzure
and use the standard "cse344" login with "Database-Course"
as password.

If needed, reminder for how to create user in a std DBMS (not SQL Azure):
create login cse444demo with password = 'isolation00userX34'
create user cse444demo for login cse444demo
use isolationtest
grant SELECT, INSERT, UPDATE, DELETE to cse444demo


