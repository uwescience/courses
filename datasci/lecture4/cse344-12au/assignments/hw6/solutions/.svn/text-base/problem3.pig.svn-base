-- Problem 3: 10 nodes, ran in about 18 minutes (5 MR jobs)
register s3n://uw-cse344-11au-code/myudfs.jar

-- Use this when debugging Problem 3
-- raw = LOAD 's3n://uw-cse344-test/cse344-test-file' USING TextLoader as (line:chararray);
-- Use this for the real run
raw = LOAD 's3n://uw-cse344/btc-2010-chunk-000' USING TextLoader as (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Use this for debugging problem 3
-- rdfabout = filter ntriples by (subject matches '.*open.*');
-- Use this for the real run
rdfabout = filter ntriples by (subject matches '.*rdfabout\\.com.*');

rdfabout2 = foreach rdfabout generate $0 as subject2:chararray, $1 as predicate2:chararray, $2 as object2:chararray;

-- Use this for debugging problem 3
-- join_result = join rdfabout by subject, rdfabout2 by subject2;
-- Use this for the real run
join_result = join rdfabout by object, rdfabout2 by subject2;

distinct_join_result = distinct join_result;
distinct_join_result_ordered = order distinct_join_result by (predicate);

store distinct_join_result_ordered into '/user/hadoop/join_results' using PigStorage();

