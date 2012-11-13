-- hw3-queries.sql
--   Queries to answer the 6 questions on the IMDB database.
-- CSE 344, homework 3 solution

-- Q1. For each movie, find the roles of actors with 5 or more roles in that movie

select distinct u.id, u.fname, u.lname, x.role, v.name, v.year
from actor u, casts x, movie v,
   (select xy.pid, xy.mid
    from casts xy
    group by xy.pid, xy.mid
    having count(distinct xy.role) > 4) y
where u.id = x.pid and x.pid = y.pid and x.mid = y.mid and x.mid = v.id and v.year = 2010
order by u.lname, u.fname;


-- Q2. For each year, find all movies with only female actors

select z.year, count(*)
from movie z
where not exists (select *
                  from actor x, casts xy
                  where x.id = xy.pid and xy.mid = z.id and x.gender!='F')
group by z.year;


-- Q3. For each year, find the percentage of movies with only female actors

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


-- MR: this version avoids three levels of query nesting
-- from xstearns' submission
SELECT m.year, (((count(m.id) - males.num) * 100.0) / count(m.id)) AS percent, count(m.id) AS total 
FROM Movie m, 
	(
	SELECT m2.year AS yr, count(DISTINCT m2.id) AS num
	FROM Movie m2, Casts c, Actor a
	WHERE c.pid = a.id AND c.mid = m2.id AND a.gender = 'M'
	GROUP BY m2.year
	) as males
WHERE m.year = males.yr	
GROUP BY m.year, males.num;

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


-- MR: this version takes only 6 seconds (as opposed to 9 mins on my machine
-- for the above)
-- From remyw's submission (modified to give the total # of movies)
select (yrs.year) as Decade_Start, yrs.total AS total_movies
	from 
		(select max(yrs.total) as maximum
			from
				(select startYr.year as year, sum(decade.amounts) as total
					from 
						(select distinct m.year as year
							from Movie m
						) as startYr,
						(select m2.year as year, count(m2.id) as amounts
							from Movie m2
							group by m2.year
						) as decade
					where decade.year >= startYr.year
						and decade.year < (startYr.year + 10)
					group by startYr.year
					order by startYr.year
				) as yrs
		) as y,
		(select startYr.year as year, sum(decade.amounts) as total
			from 
				(select distinct m.year as year
					from Movie m
				) as startYr,
				(select m2.year as year, count(m2.id) as amounts
					from Movie m2
					group by m2.year
				) as decade
			where decade.year >= startYr.year
				and decade.year < (startYr.year + 10)
			group by startYr.year
			order by startYr.year
		) as yrs
	where yrs.total = y.maximum;


-- Q6. Find actors with Kevin Bacon number 2
-- Take care to use only uncorrelated subqueries, as below

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

-- MR: this version uses EXCEPT (not shown in class)
-- and appears faster.  From dxtseng's submission.
-- No quantifiers.
select count(distinct w.b2pid) from
(select distinct c4.pid b2pid from casts c4,
(select distinct c3.mid b1mid from casts c3,
(select distinct c2.pid b1pid from casts c2,
(select distinct c.mid b0mid from actor a, casts c where a.fname='Kevin' and a.lname='Bacon' and a.id = c.pid) x
where c2.mid = x.b0mid) y
where c3.pid = y.b1pid) z where c4.mid = z.b1mid except
(select distinct c6.pid from casts c6,
(select distinct c5.mid b0mid2 from actor a2, casts c5 where a2.fname='Kevin' and a2.lname='Bacon' and a2.id = c5.pid) x2
where c6.mid = x2.b0mid2)) w;

-- MR: this version is also quite fast, and doesn't use quantifiers either.
-- From jerryzli's submission
select c2.n2 - c1.n1
from (select count (distinct c2.pid) as n2
from CASTS c2
where c2.mid in (select distinct c3.mid
from CASTS c3
where c3.pid in (select distinct c.pid
from CASTS c
where c.mid in (select c1.mid from CASTS c1 where c1.pid = 52435)))) as c2, (select count(distinct c.pid) as n1
from CASTS c
where c.mid in (select c1.mid from CASTS c1 where c1.pid = 52435)) as c1;

