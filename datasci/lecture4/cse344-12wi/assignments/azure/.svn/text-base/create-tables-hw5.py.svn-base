#!/usr/bin/python

# Paste the string with all student logins here.
# The script will generate one file.
# master.sql is the set of commands to run on the master database in SQL Azure
# IMPORTANT NOTES:
# You will need to execute each of the commands manually, one by one for each student database created
# Unfortunately, SQL Azure does not allow for granting only specific priviledges to users such as CREATE DATABASE without
# also allowing each user to delete arbitrary databases from the master.  So we must make the databases for them and allow them
# to create the tables for the assignment.

students = 'pkoutris,boonekr,lvl4l2c,msbm,jbuck15,cbutcher,jiecao2,rcarter8,omjolie,queenawc,escheung,bstalign,clinger,nickc127,davis49,doand,ledong,eastebry,emmett15,jesseg4,adh24,pingyh,krh23,dhunt925,sumanvyj,shuaij,sjonany,kalmaada,kittd,kruegerb,plai68,aglaine,hjlee513,jhl123,lym737,tlehmann,lius4,zachlum,justinm1,jpmcneal,nguyenmq,nguyen25,oliphb,brdmstr,kaiwen09,mjq,joryr,marksein,ccross59,vaspol,dcs24,satog,troyschu,catri0na,j7shen,alisayso,steelead,tlsue,swansond,talarico,acetang,bdwalker,jacwan15,huiqiw,pweisb,bxw,channie5,chiehwu,yamana25'


print "Generarating file master.sql"
fmaster = open('master2.sql','w')
for student in students.split(','):
    fmaster.write("CREATE DATABASE %sCustomer\nGOTO\n" % student)
fmaster.write("\n\n")
for student in sorted(students.split(',')):
    fmaster.write("CREATE USER %s FOR LOGIN %s;\n" % (student,student))
    fmaster.write("GRANT CREATE TABLE TO %s;\n\n" % student)
    fmaster.write("EXEC sp_addrolemember N\'db_owner\', N\'%s\'\n" % student)
fmaster.close()

print("done")
