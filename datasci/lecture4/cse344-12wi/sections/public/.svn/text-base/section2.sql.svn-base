-- CSE 344 section 2 -- more SQL review

/*** CSE 344 Section 2 database  Schema and input tuples ***/
CREATE TABLE Class (
       dept VARCHAR(6),
       number INTEGER,
       title VARCHAR(75),
       PRIMARY KEY (dept, number)
);

CREATE TABLE Instructor (
       username VARCHAR(8),
       fname VARCHAR(50),
       lname VARCHAR(50),
       started_on CHAR(10),
       PRIMARY KEY (username)
);

CREATE TABLE Teaches (
       username VARCHAR(8),
       dept VARCHAR(6),
       number INTEGER,
       PRIMARY KEY (username, dept, number),
       FOREIGN KEY (username) REFERENCES Instructor(username),
       FOREIGN KEY (dept, number) REFERENCES Class(dept, number)
);

INSERT INTO Class
       VALUES('CSE', 378, 'Machine Organization and Assembly Language');
INSERT INTO Class
       VALUES('CSE', 451, 'Introduction to Operating Systems');
INSERT INTO Class
       VALUES('CSE', 461, 'Introduction to Computer Communication Networks');

INSERT INTO Instructor VALUES('zahorjan', 'John', 'Zahorjan', '1985-01-01');
INSERT INTO Instructor VALUES('djw', 'David', 'Wetherall', '1999-07-01');
INSERT INTO Instructor VALUES('tom', 'Tom', 'Anderson', date('1997-10-01'));
INSERT INTO Instructor VALUES('levy', 'Hank', 'Levy', date('1988-04-01'));

INSERT INTO Teaches VALUES('zahorjan', 'CSE', 378);
INSERT INTO Teaches VALUES('tom', 'CSE', 451);
INSERT INTO Teaches VALUES('tom', 'CSE', 461);
INSERT INTO Teaches VALUES('zahorjan', 'CSE', 451);
INSERT INTO Teaches VALUES('zahorjan', 'CSE', 461);
INSERT INTO Teaches VALUES('djw', 'CSE', 461);
INSERT INTO Teaches VALUES('levy', 'CSE', 451);


/*
   Indexes
 */
-- SQL queries run fast on small tables, but not on big ones.
-- To make them run faster, you can use "indexes".
-- These tell you where on disk to find tuple(s) with each possible
-- value of the indexed column(s). 

-- Here, give an example of a selection and how an index speeds this up

-- Create an index of table Class, ordered by department name.
CREATE INDEX class_ix_dept ON Class(dept);
-- Can see indexes on each table with .indices table_name
-- SQLite creates some indexes automatically, usually for PRIMARY KEY cols

-- Can index multiple columns in the same index:
CREATE INDEX instructor_ix_fname_lname ON Instructor(fname, lname);
-- Then index is ordered by first column listed first, then by second
-- column listed, and so on.  This is especially useful when 
-- queries select (filter with WHERE) using mostly that combination
-- of columns; otherwise would have to read all the tuples corresponding
-- to the first column to filter by the second column, w/o an index





-- Semantics of joins:
-- FROM clause takes the Cartesian product of all the named relations.
-- WHERE conditions that relate tuples in two tables implement the join by
-- filtering the Cartesian product to only those matchings of tuples that
-- meet the conditions.

/* Review of joins */

-- Who teaches CSE 451?
SELECT i.fname, i.lname
FROM Teaches AS t, Instructor AS i
WHERE t.username = i.username AND
      t.dept = 'CSE' AND
      t.number = 451
;

-- What courses does Dr. Zahorjan teach?
SELECT c.dept, c.number
FROM Class c, Teaches t, Instructor i
WHERE c.dept = t.dept AND
      c.number = t.number AND
      t.username = i.username AND
      i.username = 'zahorjan'
;

-- Which courses do both Dr. Levy and Dr. Zahorjan teach?
SELECT c.dept, c.number, c.title
FROM Class c, Teaches t1, Teaches t2, Instructor i1, Instructor i2
WHERE c.dept = t1.dept AND c.dept = t2.dept AND
      c.number = t1.number AND c.number = t2.number AND 
      t1.username = i1.username AND
      i1.username = 'levy' AND
      t2.username = i2.username AND
      i2.username = 'zahorjan'
;
-- We can use the same table multiple times in the same query.
-- In fact, in this query, we can't use Teaches or Instructor just once.
-- Why? Because with just one of both, we'd be asking for tuples
-- where the uid is levy and zahorjan in the same tuple.
-- (Similar example from Friday's lecture: find Chinese companies
--  that make both toys and gadgets.)


/* Queries using aggregation functions */

-- How many classes are there in the course catalog?
SELECT COUNT(*)
FROM Class
;

-- What are the highest and lowest class numbers?
SELECT MIN(number), MAX(number)
FROM Class
;	

-- How many classes are being taught by at least one instructor?

-- Special case: all classes have the same department
-- First attempt - wrong!
SELECT COUNT(*) AS class_count
FROM Teaches;
-- Second attempt - also wrong
SELECT COUNT(number) AS class_count
FROM Teaches;
-- Even if you specify a column name in an aggregate function,
-- it does not eliminate duplicate values of that column, only 
-- null values.  So try this:
SELECT COUNT(DISTINCT number) AS class_count
FROM Teaches;

-- General case: this is tricky because SQL does not allow aggregation
-- functions to take more than one column as argument, unless that
-- argument is * (which only works for COUNT()).
--
-- We'll solve using subqueries and grouping - first, we group the 
-- Teaches table by department and number in a subquery, then
-- we count the number of groups in the top-level query. 
--
-- Note that we don't care what the subquery tuples are, only how many 
-- tuples/groups there are, so we return dummy tuples containing only the
-- constant 1.
--
SELECT COUNT(*) AS class_count
FROM (
  SELECT 1
  FROM Teaches
  GROUP BY dept, number
) x
;


/* Queries with both grouping and aggregation */

-- How many instructors teach each class?
SELECT dept, number, COUNT(DISTINCT username) AS teacher_count
FROM Teaches
GROUP BY dept, number
;

-- Which instructors teach more than 1 class?
-- Without grouping -- uses subquery
SELECT i.username, i.fname, i.lname
FROM Instructor i
WHERE 1 < (
  SELECT COUNT(*)
  FROM Teaches t
  WHERE t.username = i.username
)
;
-- With grouping -- no subquery
SELECT i.username
FROM Instructor i, Teaches t
WHERE i.username = t.username
GROUP BY i.username
HAVING COUNT(*) > 1
;
-- Notice that:
--  * conditions on groups go in the HAVING clause, not WHERE
--  * we dropped columns fname, lname -- how do we restore them?
-- Third version -- restores missing columns
SELECT i.username, i.fname, i.lname
FROM Instructor i, Teaches t
WHERE i.username = t.username
GROUP BY i.username, i.fname, i.lname
HAVING COUNT(*) > 1
;
-- What if we omit fname, lname from GROUP BY?  Why is that so?


/* Another subquery problem */

-- Which courses do neither Dr. Levy nor Dr. Wetherall teach?
-- wrong --- why?
SELECT c.dept, c.number, c.title
FROM Class c, Teaches t, Instructor i
WHERE c.dept = t.dept AND 
      c.number = t.number AND 
      t.username = i.username AND
      i.username NOT IN ('levy', 'djw')
;
-- This query incorrectly returns CSE 451 and 461 (twice, in fact), 
-- because there are tuples in the join where the uid is neither 
-- levy or djw, but the class is 451 and 461 -- this comes about 
-- from the fact that tom and zahorjan teach those classes.

-- Here's a corrected version that tests that the *class number* 
-- is not in the list that Hank and David teach:
SELECT *
FROM Class c
WHERE c.dept = 'CSE' AND 
      c.number NOT IN (
        SELECT c.number
        FROM Class c, Teaches t, Instructor i
        WHERE c.dept = t.dept AND c.number = t.number AND
              t.username = i.username AND
              i.username IN ('levy', 'djw')
)
;
-- This (correctly) returns only CSE 378.





/** Another database example: Population, GDP and Airports **/

/** Schema Description **/

-- A simple table for population
CREATE TABLE Population ( 
  rank INTEGER,
  country VARCHAR(30),
  population INTEGER,
  percentage FLOAT		
) ;

CREATE TABLE GDP ( 
  rank INTEGER,
  country VARCHAR(30),
  gdp INTEGER	
) ;

CREATE TABLE Airport ( 
  code VARCHAR(30),
  name VARCHAR(30),
  country VARCHAR(30)
) ;

/** import the tables in the database **/
-- .separator ,
-- .import ./population.csv Population
-- .import ./gdp.csv GDP
-- .import ./airport.csv Airport


/* Aggregation queries */

-- What is the total population of earth ?
SELECT SUM (population) AS Total_Population 
FROM Population ;

-- What is the total population of earth in billion ?
SELECT (1.00 * SUM (population)) / 1000000000 AS Total_Population 
FROM Population ;

-- What is the percentage of the population from the top 10 populated countries ?
SELECT SUM (percentage) AS Top10_Percentage
FROM Population
WHERE rank <= 10 ;

-- How many countries have less than 1 million population ?
SELECT COUNT(*) AS Small_Countries
FROM Population
WHERE population <= 1000000 ;

-- What is the GDP ratio of the average top/bottom 10 countries?
SELECT 
 (SELECT AVG(gdp) FROM GDP WHERE rank <= 10) / 
 (SELECT AVG(gdp) FROM GDP WHERE rank >= (SELECT COUNT(*) FROM GDP) -10 ) AS Rich_Poor_ratio ;


-- Which country over 10 million has the biggest GDP per capita ?
-- Be careful here, a first attempt to write the query as

--SELECT p.country, MAX(gdp)
--  FROM Population p, GDP g
--  WHERE p.country = g.country
--  AND p.population >= 10000000 ;

-- does not work (the semantics of this query are not correct, why?) 
-- Although the max(gdp) is the correct number, the country is wrong. Instead:

SELECT country, gdp 
FROM GDP g 
WHERE g.gdp = (SELECT MAX(gdp)
               FROM Population p, GDP g
               WHERE p.country = g.country AND 
                     p.population >= 10000000 
              )
;

-- Order the top 10 countries by total GDP in billion dollars
SELECT p.country, (1.00 * g.gdp * p.population) / 1000000000 AS Total_GDP 
FROM Population p, GDP g
WHERE p.country = g.country 
ORDER BY (g.gdp * p.population) DESC
LIMIT 10;

-- What percentage of the total GDP does USA have?
SELECT (100.00 * g.gdp * p.population) / (SUM (i.total_gdp) ) AS USA_percentage
FROM (SELECT p.country AS country, (g.gdp * p.population) AS total_gdp
      FROM Population p, GDP g
      WHERE p.country = g.country ) AS i, Population p, GDP g
WHERE p.country = 'United States' AND g.country = p.country ;


-- Top 10 countries with most international airports
SELECT country, COUNT(*) 
FROM Airport
GROUP BY country 
ORDER BY COUNT(*) DESC 
LIMIT 10 ; 

-- Top 10 countries with most international airports per people
SELECT p.country, n.num_airports 
FROM Population p,  (SELECT country, COUNT(*) AS num_airports 
                     FROM Airport 
                     GROUP BY country) n
WHERE n.country = p.country AND 
      p.population >= 1000000
ORDER BY (1.00 * n.num_airports) / (p.population) DESC
LIMIT 10 ; 


-- How many countries have more than 500 airports ?
-- Nesting a SQL statement: the subquery returns 
SELECT COUNT(*) AS country_count
FROM (
  SELECT 1
  FROM Airport
  GROUP BY country
  HAVING COUNT(*) >= 500
) x ;


-- How many countries have airports?
-- Be careful here, we need the DISTINCT keyword to make this work correctly
SELECT COUNT (DISTINCT country) 
FROM Airport ;


