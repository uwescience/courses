-- Problem 4: compute the histogram for the entire dataset
register s3n://uw-cse344-code/myudfs.jar
raw = LOAD 's3n://uw-cse344' USING TextLoader as (line:chararray);
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray) PARALLEL 50;
subjects = group ntriples by (subject) PARALLEL 50;
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;
group_subject_by_count = group count_by_subject by (count) PARALLEL 50;
count_subject_by_count = foreach group_subject_by_count generate flatten($0) as countval, COUNT($1) as num_subj  PARALLEL 50;
count_subject_by_count_ordered = order count_subject_by_count by countval  PARALLEL 50;
store count_subject_by_count_ordered into 's3n://query-output/problem4';
