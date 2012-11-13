-- Problem 2
register s3n://uw-cse344-11au-code/myudfs.jar

-- For Problem 2A
raw = LOAD 's3n://uw-cse344-test/cse344-test-file' USING TextLoader as (line:chararray);

-- For Problem 2B
-- raw = LOAD 's3n://uw-cse344/btc-2010-chunk-000' USING TextLoader as (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

subjects = group ntriples by (subject);
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as countval;
group_subj_by_count = group count_by_subject by (countval);
count_subj_by_count = foreach group_subj_by_count generate flatten($0) as countval, COUNT($1) as num_subj;
count_subj_by_count_ordered = order count_subj_by_count by countval;
store count_subj_by_count_ordered into '/user/hadoop/histogram' using PigStorage();
