<Enrollment>
  { for $n in doc("problem2b.xml")/Normalized,
    $s in $n/students/student
    return <student>
             { $s/name,
               $s/address,
               for $e in $n/takes/take[name=$s/name],
                   $c in $n/courses/course[title=$e/title]
               return <course>
                        { $c/title,
                          $c/instructor,
                          $e/grade
                        }
                      </course>
              }
           </student>
   }
</Enrollment>
