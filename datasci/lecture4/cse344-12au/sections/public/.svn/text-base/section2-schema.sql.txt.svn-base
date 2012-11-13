/*** CSE 344 Section 1 database -- for section 2 ***/

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
