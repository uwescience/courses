-- create-indexes.sql
--   Creates indexes to make queries run fast 
--   on the database of create-tables.sql.
-- CSE 344, homework 2 solution

create unique index movieid on movie(id);
create index moviename on movie(name);
create unique index actorid on actor(id);
create index actorlname on actor(lname);

create index castsmid on casts(mid);
create index castspid on casts(pid);
create unique index directorsid on directors(id);
create index directorslname on directors(lname);
create index moviedirectorsmid on movie_directors(mid);
create index moviedirectordid on movie_directors(did);
CREATE index movieyear ON movie(year);
