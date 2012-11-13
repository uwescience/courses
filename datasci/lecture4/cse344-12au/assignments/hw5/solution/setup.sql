--kmorton: Order matters when dropping tables.  Drop child tables first
--to avoid errors in constraints.
drop table MovieRentals;
drop table Customers;
drop table RentalPlans;

CREATE TABLE RentalPlans(
  pid integer PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL,
  max_movies int NOT NULL,
  fee numeric(6,2) NOT NULL
);

CREATE TABLE Customers(
  cid integer PRIMARY KEY,
  login VARCHAR(50),
  password VARCHAR(50),
  fname VARCHAR(50),
  lname VARCHAR(50),
  pid integer REFERENCES RentalPlans (pid)
);


CREATE TABLE MovieRentals(
  mid integer NOT NULL,
  cid integer REFERENCES Customers(cid),
  date_out DATETIME NOT NULL, 
  status VARCHAR(10) CHECK (status = 'open' or status = 'closed')
);
--kmorton: Required by SQL Azure before you can insert into table that does
--not have the primary key specified
Create clustered index movieIndex on MovieRentals(mid);


INSERT INTO RentalPlans VALUES (1, 'basic', 1, 1.99);
INSERT INTO RentalPlans VALUES (2, 'rental plus', 3, 2.99);
INSERT INTO RentalPlans VALUES (3, 'super access', 5, 3.99);
INSERT INTO RentalPlans VALUES (4, 'prime', 10, 4.99);

INSERT INTO Customers VALUES (1, 'george', '123', 'George', 'Ford', 1);
INSERT INTO Customers VALUES (2, 'tim', 'secret', 'Tim', 'Johnson', 1);

INSERT INTO MovieRentals VALUES(22592, 1,  '2011-03-20 11:32:14', 'open');
INSERT INTO MovieRentals VALUES(22591, 1,  '2011-04-02 19:17:55', 'closed');



INSERT INTO RentalPlans VALUES (1, 'basic', 1, 1.99);
INSERT INTO RentalPlans VALUES (2, 'rental plus', 3, 2.99);
INSERT INTO RentalPlans VALUES (3, 'super access', 5, 3.99);
INSERT INTO RentalPlans VALUES (4, 'prime', 10, 4.99);

INSERT INTO Customers VALUES (1, 'george', '123', 'George', 'Ford', 1);
INSERT INTO Customers VALUES (2, 'tim', 'secret', 'Tim', 'Johnson', 1);

INSERT INTO MovieRentals VALUES(22592, 1,  '2011-03-20 11:32:14', 'open');
INSERT INTO MovieRentals VALUES(22591, 1,  '2011-04-02 19:17:55', 'closed');
