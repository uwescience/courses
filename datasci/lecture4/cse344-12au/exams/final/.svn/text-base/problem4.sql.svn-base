create table R (A int, B int);
insert into R values(1,10);
insert into R values(2,20);

-- TIMESTAMP 1
-- T1
begin transaction; 

-- TIMESTAMP 2
-- T1
select * from R;

-- TIMESTAMP 3
-- T2
begin transaction;

-- TIMESTAMP 4
-- T2
select * from R where A=2;
-- returns value 20

-- TIMESTAMP 5
-- T1
update R set B=30 where A=2;

-- TIMESTAMP 6
-- T2
select * from R where A=2;
-- on sqlite: returns old value 20
-- on sqlserver: waits until after time stamp 7

-- TIMESTAMP 7
-- T1
commit;
-- on sqlite: database is locked!  Need to retry on Step 11
-- on sqlsever: success; T2 returns new value 30

-- TIMESTAMP 8
-- T3
begin transaction;

-- TIMESTAMP 9
-- T3
select * from R where A=2;
-- on sqlite: database is locked!  Need to retry on Step 12
-- on sqlsever: success, returns new value 30

-- TIMESTAMP 10
-- T2
commit;
-- success

-- TIMESTAMP 11
-- T1
-- on sqlite only:
commit;

-- TIMESTAMP 12
-- T3
-- on sqlite only
select * from R where A=2;

-- TIMESTAMP 13
-- on both
commit;
-- on sqlite: returns new value 30