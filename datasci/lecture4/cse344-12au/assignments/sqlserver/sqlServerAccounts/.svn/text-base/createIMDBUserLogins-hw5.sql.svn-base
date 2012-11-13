DECLARE @UserString varchar(8000)
DECLARE @DatabaseString varchar(8000)
DECLARE @DefaultDatabase varchar(255)

DECLARE @delimiter char(1)
 
SET @UserString = 'mickayz,cjbento,capaloto,tsing,jinoue3,nikhilk,kainby87,narakim,knappg,lmccrea,menzs,jtn75,nigussm,nilk,hsp3,dreinelt,engobada,shihwy,alnith,bkw7,jkwong89,keith619,mlidge,cjordan1,kaulichr,daseul,mmoyers,karynne7,shenz,kunw,wyizhou,aweigeri'

SET @DatabaseString = 'master'
SET @DefaultDatabase = 'master'

SET @delimiter = ','
BEGIN TRY
    DROP TABLE #Users
    DROP TABLE #Databases
    DROP TABLE #Roles
END TRY BEGIN CATCH END CATCH
 
    ;WITH Substr(num, firstchar, lastchar) AS (
      SELECT 1, 1, CHARINDEX(@delimiter, @UserString)
      UNION ALL
      SELECT num + 1, lastchar + 1, CHARINDEX(@delimiter, @UserString, lastchar + 1)
      FROM Substr
      WHERE lastchar > 0
    )
    SELECT
        num,
        UserName = SUBSTRING(@UserString, firstchar, CASE WHEN lastchar > 0 THEN lastchar-firstchar ELSE 8000 END)
    INTO #Users
    FROM Substr
 
    ;WITH Substr(num, firstchar, lastchar) AS (
      SELECT 1, 1, CHARINDEX(@delimiter, @DatabaseString)
      UNION ALL
      SELECT num + 1, lastchar + 1, CHARINDEX(@delimiter, @DatabaseString, lastchar + 1)
      FROM Substr
      WHERE lastchar > 0
    )
    SELECT
        num,
        DatabaseName = SUBSTRING(@DatabaseString, firstchar, CASE WHEN lastchar > 0 THEN lastchar-firstchar ELSE 8000 END)
    INTO #Databases
    FROM Substr
 
    ;
 
DECLARE @NumUsers int
DECLARE @NumDBs int
DECLARE @UserIter int
DECLARE @DBIter int

DECLARE @UserName varchar(255)
DECLARE @DBName varchar(255)

DECLARE @SQL varchar(max)
 
SET @NumUsers   = (SELECT MAX(num) FROM #Users)
SET @NumDBs     = (SELECT MAX(num) FROM #Databases)
SET @UserIter   = 1
SET @SQL        = ''
 
WHILE @UserIter <= @NumUsers
BEGIN
    SET @DBIter     = 1
  
    
    SET @UserName = (SELECT UserName FROM #Users WHERE num = @UserIter)
    
    SET @UserIter = @UserIter + 1
    -- Add user to the databases
    WHILE @DBIter <= @NumDBs
    BEGIN
        SET @DBName = (SELECT DatabaseName FROM #Databases WHERE num = @DBIter)
        SET @SQL = 'USE ' + @DBName + '; CREATE USER ' + @UserName + ' FOR LOGIN ' + @UserName
        PRINT (@SQL)
        SET @SQL = 'USE ' + @DBName + '; GRANT CREATE DATABASE to ' + @UserName 
        PRINT (@SQL)
        SET @DBIter = @DBIter + 1
        
    END
END

