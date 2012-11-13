<trips>
{
  for $d in doc("trips.xml")/trips
  for $x in distinct-values( $d//airline/text())

  return 
    <airline>
      <name> {$x} </name>
      {
      for $y in $d/personal | $d/business 
      where $y/airline/text() = $x
      return 
           <trip> { $y/@destination } 
             <stops>{ count($y/stops/location) }</stops>
           </trip>
      }
   </airline>
}
</trips>