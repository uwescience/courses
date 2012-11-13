How to use SQL Server Users creation script
1) Open createIMDBUserLogins.sql
2) Change the @UserString to be a comma-delimited list of usernames, as in the example within the script itself. Their password is set near the bottom of the file with @Password, and is currently SQLcsep544
3) Execute the query. The result will be a set of SQL statements.
4) Copy the resulting SQL statements, and run those SQL statements.
