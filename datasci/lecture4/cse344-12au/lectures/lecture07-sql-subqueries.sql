--------------------------------------------------------------------------------
-- CSE 344 -- Winter 2012
-- Lecture 07: SUBQUERIES IN SQL
--------------------------------------------------------------------------------
-- run these queries in SQL Lite or in SQL Azure

-- for sqllite only:
.headers on
.mode columns

create table Product(pname varchar(30) primary key, price int, cid int);
create table Company(cid int primary key, cname varchar(10), city varchar(10));
insert into Product values ('gizmo', 100, 1);
insert into Product values('powergizmo', 200, 1);
insert into Product values('iStuff', 500, 2);
insert into Product values('gadget', 300, 2);
insert into Product values('powergadget', 400, 2);
insert into Company values(1,'GizmoWorks','San Jose');
insert into Company values(2,'BigCompany','Boston');
insert into Company values(3,'PowerWorks','Seattle');

--------------------------------------------------------------------------------
-- 1. subqueries in Select:

SELECT X.pname, (SELECT Y.city FROM Company Y WHERE Y.cid=X.cid) as City
FROM  Product X;

-- same as:

SELECT X.pname, Y.city
FROM   Product X, Company Y
WHERE X.cid=Y.cid;


-- Compute the number of products made by each company:

SELECT DISTINCT C.cname, (SELECT count(*) FROM Product P WHERE P.cid=C.cid)
FROM  Company C;

SELECT C.cname, count(*)
FROM Company C, Product P
WHERE C.cid=P.cid
GROUP BY C.cname;
-- they are not exactly equivalent! why?


-- are these queries equivalent? Try them out!

SELECT DISTINCT C.cname, (SELECT count(*) FROM Product P WHERE P.cid=C.cid)
FROM  Company C;

SELECT C.cname, count(*)
FROM Company C, Product P
WHERE C.cid=P.cid
GROUP BY C.cname;

SELECT C.cname, count(pname)
FROM Company C LEFT OUTER JOIN Product P
ON C.cid=P.cid
GROUP BY C.cname;

--------------------------------------------------------------------------------
-- 2. subqueries in From:

SELECT X.pname FROM (SELECT * FROM Product AS Y WHERE price > 20) as X
WHERE X.price < 500;

--------------------------------------------------------------------------------
-- 3. subqueries in Where

-- Find all companies that make some products with price < 200
SELECT DISTINCT  C.cname
FROM     Company C
WHERE  EXISTS (SELECT * FROM Product P WHERE C.cid = P.cid and P.price < 200);

SELECT DISTINCT  C.cname
FROM     Company C
WHERE C.cid IN (SELECT P.cid FROM Product P WHERE P.price < 200);

-- Find all companies that make only products with price < 200

-- Step 1. Find the other companies: i.e. s.t. some product >= 200

SELECT DISTINCT  C.cname
FROM     Company C
WHERE  C.cid IN (SELECT P.cid FROM Product P WHERE P.price >= 200);

-- Step 2. Find all companies s.t. all their products have price < 200

SELECT DISTINCT  C.cname
FROM     Company C
WHERE  C.cid NOT IN (SELECT P.cid FROM Product P WHERE P.price >= 200);


-- Altenratively:
-- Step 1 using 'exists':

SELECT DISTINCT  C.cname
FROM     Company C
WHERE EXISTS (SELECT * FROM Product P WHERE P.cid = C.cid and P.price >= 200);

-- Step 2 using 'not exists':

SELECT DISTINCT  C.cname
FROM     Company C
WHERE  EXISTS (SELECT * FROM Product P WHERE P.cid = C.cid and P.price >= 200);


----------------------------------------------------------------------
-- Unnesting aggregates

-- equivalent queries:
SELECT DISTINCT city, (SELECT count(*) FROM Company Y WHERE X.city = Y.city)
FROM  Company X;

SELECT city,  count(*)
FROM   Company 
GROUP BY city;


-- non-equivalent queries (why?)
SELECT DISTINCT X.city, (SELECT count(*) FROM Product Y, Company Z WHERE Z.cid=Y.cid
				 AND Z.city = X.city)
FROM  Company X;


SELECT X.city, count(*)
FROM Company X, Product Y
WHERE X.cid=Y.cid GROUP BY X.city;

-- For each city, find the most expensive product made in that city

-- Finding the maximum price is easy…

SELECT x.city, max(y.price)
FROM Company x, Product y
WHERE x.cid = y.cid
GROUP BY x.city;

SELECT DISTINCT u.city, v.pname, v.price
FROM Company u, Product v,
     (SELECT x.city, max(y.price) as maxprice
      FROM Company x, Product y
      WHERE x.cid = y.cid
      GROUP BY x.city) w
WHERE u.cid = v.cid
 and u.city = w.city
 and v.price=w.maxprice;
-- do we neeed DISTINCT?

-- another, more concise solution:

SELECT u.city, v.pname, v.price
FROM Company u, Product v, Company x, Product y
WHERE u.cid = v.cid and u.city = x.city and x.cid = y.cid
GROUP BY u.city, v.pname, v.price
HAVING v.price = max(y.price);

-- and also

SELECT u.city, v.pname, v.price
FROM Company u, Product v
WHERE u.cid = v.cid
  and v.price >= ALL (SELECT y.price FROM Company x, Product y WHERE u.city=x.city and x.cid=y.cid);