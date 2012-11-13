#!/usr/bin/python

# Paste the string with all student logins here.
# The script will generate two files.
# master.sql is the set of commands to run on the master database in SQL Azure
# imbdb.sql is the set of commands to run on the imdb database.
# Paris: I had some problems with issuing batch CREATE user, so I modified the script to add the batch separator GO
students = 'boonekr,lvl4l2c,msbm,jbuck15,cbutcher,jiecao2,rcarter8,omjolie,queenawc,escheung,bstalign,clinger,nickc127,davis49,doand,ledong,eastebry,emmett15,jesseg4,adh24,pingyh,krh23,dhunt925,sumanvyj,shuaij,sjonany,kalmaada,kittd,kruegerb,plai68,aglaine,hjlee513,jhl123,lym737,tlehmann,lius4,zachlum,justinm1,jpmcneal,nguyenmq,nguyen25,oliphb,brdmstr,kaiwen09,mjq,joryr,marksein,ccross59,vaspol,dcs24,satog,troyschu,catri0na,j7shen,alisayso,steelead,tlsue,swansond,talarico,acetang,bdwalker,jacwan15,huiqiw,pweisb,bxw,channie5,chiehwu,yamana25'

password = 'SQLcse344'

print "Generarating file master.sql"
fmaster = open('master.sql','w')
for student in students.split(','):
    fmaster.write("CREATE LOGIN %s WITH PASSWORD=N\'%s\'\nGO\n" % (student, password))
    fmaster.write("CREATE USER %s FOR LOGIN %s\nGO\n" % (student,student))
fmaster.close()

print "Generating file imdb.sql"
fimdb = open('imdb.sql','w')
for student in students.split(','):
    fimdb.write("CREATE USER %s FOR LOGIN %s\nGO\n" % (student,student))
    fimdb.write("EXEC sp_addrolemember N\'db_datareader\',N\'%s\'\n" % student)
    fimdb.write("GRANT SHOWPLAN TO %s\nGO\n" % student)
fimdb.close()

print("done")
