-- hw3-queries.sql
--   Queries to answer the 6 questions on the IMDB database.
-- CSE 344, homework 3 solution

-- Q1. For each movie, find the roles of actors with 5 or more roles in that movie
-- 137 rows
select distinct u.id, u.fname, u.lname, x.role, v.name, v.year
from actor u, casts x, movie v,
   (select xy.pid, xy.mid
    from casts xy
    group by xy.pid, xy.mid
    having count(distinct xy.role) > 4) y
where u.id = x.pid and x.pid = y.pid and x.mid = y.mid and x.mid = v.id and v.year = 2010
order by u.lname, u.fname;


-- Q2. For each year, find all movies with only female actors
--129 rows
select z.year, count(*)
from movie z
where not exists (select *
                  from actor x, casts xy
                  where x.id = xy.pid and xy.mid = z.id and x.gender!='F')
group by z.year;


-- Q3. For each year, find the percentage of movies with only female actors
-- 128 rows
select a.year, a.c*100.00/b.c as percentage, b.c as total_overall
from (select z.year, count(*) as c
      from movie z
      where not exists (select *
                        from actor x, casts xy
                        where x.id = xy.pid and xy.mid = z.id and x.gender!='F')
      group by z.year) a,
     (select z.year, count(*) as c from movie z group by z.year) b
where a.year=b.year
order by a.year;


-- Q4. Find the movie(s) with the largest cast

select x.name, count(distinct xy.pid) as c
from movie x, casts xy
where x.id = xy.mid
group by x.id, x.name
having not exists (select u.id
                   from movie u, casts uv
                   where u.id=uv.mid
                   group by u.id
                   having count(distinct uv.pid) > count(distinct xy.pid));

-- same query, a notch faster
select x.name, count(distinct xy.pid) as c
from movie x, casts xy
where x.id = xy.mid
group by x.id, x.name
having count(distinct xy.pid) >= all
       (select count(distinct uv.pid)
        from movie u, casts uv
        where u.id=uv.mid
        group by u.id);


-- Q5. Find the decade with the most movies
--year 2000 with 457,481 movies
select y.year, count(*)
from (select distinct x.year from movie x) y,
     movie z
where y.year <= z.year and z.year < y.year+10
group by y.year
having not exists (select y1.year
                   from (select distinct x1.year from movie x1) y1, movie z1
                   where y1.year <= z1.year and z1.year < y1.year+10
                   group by y1.year
                   having count(z1.id) > count(z.id));


-- Q6. Find actors with Kevin Bacon number 2
-- Take care to use only uncorrelated subqueries, as below
--521,876
select  count(distinct c2.pid)
from    Actor a0, Casts c0, Casts c1a, Casts c1b, Casts c2
-- c0.pid is Kevin Bacon
-- c1.pid has BN=1
-- c2.pid has BN=2
where  a0.fname = 'Kevin' AND a0.lname = 'Bacon'
   AND a0.id   = c0.pid   -- pid0 = Kevin Bacon
   AND c0.mid  = c1a.mid  -- pid0 and pid1 acted in the same movie
   AND c1b.pid = c1a.pid  -- same actor pid1
   AND c1b.mid = c2.mid   -- pid1 and pid2 acted in the same movie
   AND c2.pid NOT IN       -- c2.pid does not have KN=1 or KN=0
        (select d1.pid    -- Note the subquery must be uncorrelated !  Otherwise time=forever
         from  Actor b0, Casts d0, Casts d1
         where b0.fname = 'Kevin' AND b0.lname = 'Bacon'
           AND b0.id  = d0.pid -- d0.pid  = Kevin Bacon
           AND d0.mid = d1.mid -- d0.pid and d1.pid acted in the same movie
        );
