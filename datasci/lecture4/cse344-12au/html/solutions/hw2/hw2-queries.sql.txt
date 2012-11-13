-- hw2-queries.sql
--   Queries to answer the 5 questions on the IMDB database.
-- CSE 344, homework 2 solution

-- Q1
select x.fname, x.lname
from actor x, casts xy, movie y
where x.id = xy.pid and xy.mid = y.id and y.name = 'Officer 444';

-- Q2
select x.id, x.fname, x.lname, y.name, y.year
from directors x, movie_directors xy, movie y, genre z
where x.id = xy.did and xy.mid = y.id and (y.year/4)*4=y.year and y.id = z.mid and z.genre='Film-Noir';


--Q3 Note: need to have index on movie(year)
select distinct x.fname, x.lname
from actor x, casts xy, casts xz, movie y, movie z
where x.id = xy.pid and x.id = xz.pid
  and xy.mid = y.id and xz.mid = z.id
  and y.year < 1900 and z.year > 2000;

-- Investigation:

select distinct x.fname, x.lname, xy.role, xz.role
from actor x, casts xy, casts xz, movie y, movie z
where x.id = xy.pid and x.id = xz.pid
  and xy.mid = y.id and xz.mid = z.id
  and y.year < 1900 and z.year > 2000;

-- most roles are "himself": these are historical figures (Theodore
-- Roosevelt, the Tsar, etc) who are listed as actors in documentaries
-- made both in the past and very recently


-- Q4 Directors with over 500 movies
select x.fname, x.lname, count(*) as c
from directors x, movie_directors y
where x.id = y.did
group by x.id, x.fname, x.lname
having count(*) >= 500
order by c desc;

-- Q5   Actors with five or more roles;  note: need index on movie(year)
select x.fname, x.lname, y.name, count(distinct xy.role) as c
from actor x, casts xy, movie y
where x.id = xy.pid and xy.mid = y.id and y.year = 2010
group by x.id, x.fname, x.lname, y.id, y.name
having count(distinct xy.role) > 4
order by c desc;

