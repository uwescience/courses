/*
This is a runnable solution to HW1 for CSE344. All the SQL and SQLite commands 
necessary to complete the homework are included. To see the output along with
the commands, look at hw1_solution.txt or run this file in SQLite.
*/

drop table if exists R;
drop table if exists MyRestaurants;

.echo on

/* Problem 1,a */
create table R(A int, B int);

/* Problem 1,b */
insert into R values (2,4);
insert into R values(1,1);
insert into R values (3,2);

/* Problem 1,c */
select * from R;

/* Problem 1,d */
/* We don't get an error because the strings are interpreted as ints (SQLite uses dynamic typing) */
/* Additionally, unlike other existing DBMSs, where each column is associated with a type and can only hold data */
/* of that given type, in SQLite, any column can hold any type of data. See: http://www.sqlite.org/datatype3.html */
/* for details. */
insert into R values ('5','2');
select * from R;

/* Problem 1,e */
select A from R;

/* Problem 1,f */
select * from R where A <= B;

/* Problem 2 */
create table MyRestaurants(name varchar(50), food_type varchar(50), distance int, last_visit varchar(10),like_it int);

/* Problem 3 */
insert into MyRestaurants values ('McDonald''s','fast food',30,'2011-03-23',1);
insert into MyRestaurants values ('Chipotle','mexican',15,'2011-02-15',0);
insert into MyRestaurants values ('Burger Burger','fast food',15,'2011-03-15',1);
insert into MyRestaurants values ('Olive Garden','italian',30,'2011-03-24',1);
insert into MyRestaurants values ('Arby''s','fast food',45,'2010-06-15',0);
insert into MyRestaurants values ('University Teriyaki','teriyaki',15,'2010-06-30',NULL);

/* Problem 4 */
select * from MyRestaurants;

/* Problem 5,a */
.mode csv
select * from MyRestaurants;

/* Problem 5,b */
.mode list
.separator " | "
select * from MyRestaurants;

/* Problem 5,c */
.mode column
.width 15 15 15 15 15
select * from MyRestaurants;

/* Problem 5,d */
.headers on
.mode csv
select * from MyRestaurants;

.mode list
.separator " | "
select * from MyRestaurants;

.mode column
.width 15 15 15 15 15
select * from MyRestaurants;         

/* Problem 6 */
select *, case when like_it = 1 then 'I liked it' when like_it = 0 then 'I hated it' end as iLike from MyRestaurants;         

/* Problem 7 */
/* inserting tuple just so we can see that it works */
insert into MyRestaurants values ('Old Spaghetti Factory','italian',45,'2010-06-15',1);
select * from MyRestaurants where like_it =1 and date(last_visit) < date('now','-3 month');   
select * from MyRestaurants where like_it =1 and last_visit < date('now','-3 month');

