-- create-tables.sql
--   Imports the IMDB movie dataset into the current database.
-- CSE 344, homework 2 solution

create table actor(id int PRIMARY KEY, fname varchar(30), lname varchar(30), gender char(1));
create table movie(id int PRIMARY KEY, name varchar(150), year int);
create table directors(id int PRIMARY KEY, fname varchar(30), lname varchar(30));

create table genre(mid int, genre varchar(50));
create table casts(pid int REFERENCES actor, mid int REFERENCES movie, role varchar(50));
create table movie_directors(did int REFERENCES directors, mid int REFERENCES movie);

.import 'imdb2010/actor.txt' actor
.import 'imdb2010/movie.txt' movie
.import 'imdb2010/casts.txt' casts
.import 'imdb2010/directors.txt' directors
.import 'imdb2010/genre.txt' genre
.import 'imdb2010/movie_directors.txt' movie_directors
