register ./myudfs.jar

-- Problem 1
--raw = LOAD 's3n://uw-cse344-test/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD 's3n://uw-cse344/btc-2010-chunk-000' USING TextLoader as (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
--ntriplesf = filter ntriples by not (subject matches 'junk');

-- Problem 2
--Question being asked: group the n-triples by subject and return the counts for each subject in descending order.
--Then group this list by counts, to get the set of subjects that had that particular count
--grouping, counting and sorting for subject

subjects = group ntriples by (subject);
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as countval;
group_subj_by_count = group count_by_subject by (countval);
count_subj_by_count = foreach group_subj_by_count generate flatten($0) as countval, COUNT($1) as num_subj;
count_subj_by_count_ordered = order count_subj_by_count by countval;
store count_subj_by_count_ordered into '/user/hadoop/histogram' using PigStorage();


---  this seems obsolete now; delete ??
----Question being asked: group the n-triples by object and return the counts for each object in descending order
----grouping,counting and sorting for object (redundant)
--objects = group ntriplesf by (object);
--count_by_object = foreach objects generate flatten($0), COUNT($1) as count;
--count_by_object_ordered = order count_by_object by (count) desc;
--dump count_by_object_ordered;

-- Same here, seems obsolete
----Question being asked: group the n-triples by subject and return the counts for each subject with a GLN starting with 0 in descending order
----example of a GLN starting with 0: <http://openean.kaufkauf.net/id/businessentities/GLN_0166620000056> (confusing)
----filtering,grouping,counting and sorting for subject
--filtered = filter ntriples by (subject matches '.*GLN_0.*');
--subjects_filtered = group filtered by (subject);
--count_by_subject_filtered = foreach subjects_filtered generate flatten($0), COUNT($1) as count;
--count_by_subject_ordered_filtered = order count_by_subject_filtered by (count) desc;
--dump count_by_subject_ordered_filtered;


-- Problem 3
--Question being asked: do a join on subject=object
--untested right now. I just added the twitter filter. But I did make sure that there are twitter tuples in 
--btc-2010-chunk-000

rdfabout = filter ntriples by (subject matches '.*rdfabout\\.com.*');
rdfabout2 = foreach rdfabout generate $0 as subject2:chararray, $1 as predicate2:chararray, $2 as object2:chararray;

join_result = join rdfabout by subject, rdfabout2 by object2;
distinct_join_result = distinct join_result;
distinct_join_result_ordered = order distinct_join_result by (predicate);
store distinct_join_result_ordered into '/user/hadoop/join_results' using PigStorage();


-- Problem 4
-- Question being asked: compute the histogram for the entire dataset (need to check this)
-- Leilani the query below does somethign much simpler.  It took 2hours and 40minutes.  All this time was taken by the MAP tasks: the reduce tasks were instantaneous.
-- can you please modify it to compute the histogram; do not run it: I plan to test it Friday morning.
-- My hope is that the histogram will not take much longer than computing the outdegrees
register ./myudfs.jar
raw = LOAD 's3n://uw-cse344' USING TextLoader as (line:chararray);
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
filtered = filter ntriples by (subject matches '.*GLN_0.*');
subjects = group filtered by (subject);
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count;
store count_by_subject into 's3n://query-output/test';

-- Problem 4
-- new version for histogram information
register ./myudfs.jar
raw = LOAD 's3n://uw-cse344' USING TextLoader as (line:chararray);
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
filtered = filter ntriples by (subject matches '.*GLN_0.*');
subjects = group filtered by (subject);
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count;
group_subject_by_count = group count_by_subject by (count);
count_subject_by_count = foreach group_subject_by_count generate flatten($0) as countval, COUNT($1) as num_subj;
count_subject_by_count_ordered = order count_subject_by_count by countval;
store count_subject_by_count_ordered into 's3n://query-output/test';
--store count_subject_by_count_ordered into 'user/hadoop/problem4';