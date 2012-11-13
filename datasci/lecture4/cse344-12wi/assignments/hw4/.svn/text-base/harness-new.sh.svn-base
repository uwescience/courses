#!/bin/bash
#Uses diffxml.sh which can be downloaded from here: http://sourceforge.net/projects/diffxml/files/diffxml/0.95%20BETA/diffxml-0.95B.zip/download

#userdir='/Users/kmorton/Documents/cse344/CSE 344 Homework Dropbox/Homework # 4 Turn in Nov 4 on time'
#userdir='/Users/kmorton/Documents/cse344/CSE 344 Homework Dropbox/Homework # 4 Turn in Nov 5 1 day late' 
userdir='/Users/kmorton/Documents/cse344/CSE 344 Homework Dropbox/Homework # 4 Turn in Nov 6 2 days late'
solndir='/Users/kmorton/Documents/cse344/cse344-11au/assignments/hw4/solution/'

for user in `find "$userdir" -type d -maxdepth 1 -mindepth 1 -exec basename {} \\;`
do
  echo "Processing user $user"
  echo `cp $solndir/mondial* "$userdir/$user"`
  i=1;
  for filename in `find "$userdir/$user/" -maxdepth 1 -iname "*.xq" -exec basename {} \\; | sort`
  do
    bn=`basename "$filename" .xq` 
    echo "  Evaluating $user/$bn"

    xqfile="$userdir/$user/$bn.xq"
    xmlfile="$userdir/$user/$bn.xml"
    difffile="$userdir/$user/$bn.xml.diff"

    #echo "  Executing as: java -cp /Users/kmorton/Documents/cse344/cse344-11au/lectures/XML-LECTURE-QUERIES/saxon9he.jar net.sf.saxon.Query '$xqfile' > '$xmlfile' 2>&1"
    echo `java -cp /Users/kmorton/Documents/cse344/cse344-11au/lectures/XML-LECTURE-QUERIES/saxon9he.jar net.sf.saxon.Query "$xqfile" > "$xmlfile" 2>&1`

    echo "  Comparing $bn.xml to solution/Problem$i.xml"
    diffresults=`/Users/kmorton/Downloads/diffxml/diffxml.sh -q "$solndir/Problem$i.xml" "$xmlfile"`
    if echo $diffresults | grep -qE "XML documents .* differ"
    then
      `/Users/kmorton/Downloads/diffxml/diffxml.sh "$solndir/Problem$i.xml" "$xmlfile" > "$difffile"`
      `xmllint --format "$xmlfile" > "$userdir/$user/$bn.cleaned.xml"`
      `xmllint --format "$solndir/Problem$i.xml" > "$solndir/Problem$i.cleaned.xml"`
      echo "    !! FAILED !!"
      echo "    Diff results: \"$difffile\""
      echo "    Pretty comparison: sdiff \"$solndir/Problem$i.cleaned.xml\" \"$userdir/$user/$bn.cleaned.xml\""
    fi
    echo
    let i+=1
  done;
done;

