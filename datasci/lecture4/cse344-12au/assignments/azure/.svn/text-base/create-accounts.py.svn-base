#!/usr/bin/python

# Paste the string with all student logins here.
# The script will generate two files.
# master.sql is the set of commands to run on the master database in SQL Azure
# imbdb.sql is the set of commands to run on the imdb database.
# Because one cannot issue batch CREATE user, the script adds the batch separator GO
students = 'abboudm,abykov,agale,aosobov,apacible,bing04,bkgomez,cartma,casw123,caylan,cgt2,cmoice,crovillo,csquared,davejung,donohueb,edc4,ewhite12,hatjatji,jacobs22,jamesl33,jcwr,jialehe,jmnumata,josephs,jvh23,jyo2,kaz21,kevint15,kevinxd3,kristini,ktang92,lee33,leelee,liuj7,lkrystal,lzornes,mahh,mengwan,michelim,muelkiel,munutzer,mzhou,olehg,pbhuss,peixin,sahabp,snwang,styner,tolisker,tonywho,wangs5,wangy24,wcsmith,weimiz,winglam,wmgannon,xinx,yoongk'

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

