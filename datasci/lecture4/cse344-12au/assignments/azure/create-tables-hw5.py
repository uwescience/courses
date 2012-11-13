#!/usr/bin/python

# Paste the string with all student logins here.
# The script will generate one file.
# master.sql is the set of commands to run on the master database in SQL Azure
# IMPORTANT NOTES:
# You will need to execute each of the commands manually, one by one for each student database created
# Unfortunately, SQL Azure does not allow for granting only specific priviledges to users such as CREATE DATABASE without
# also allowing each user to delete arbitrary databases from the master.  So we must make the databases for them and allow them
# to create the tables for the assignment.

students = 'magda,vaspol,mmoyers,shenz,abboudm,apacible,bing04,abykov,edc4,cartma,cll07,chrisc36,kevinxd3,donohueb,allyg02,wmgannon,olehg,bkgomez,jialehe,tonywho,pbhuss,ivarsonk,davejung,muelkiel,yoongk,winglam,caylan,jamesl33,lee33,michelim,liuj7,mahh,cmoice,styner,jmnumata,jyo2,tolisker,aosobov,jcwr,crovillo,sahabp,jacobs22,josephs2,wcsmith,ktang92,kevint15,cgt2,hatjatji,munutzer,jvh23,mengwan,wangs5,snwang,wangy24,ewhite12,casw123,lkrystal,xinx,peixin,kaz21,weimiz,mzhou,lzornes'


print "Generarating file master.sql"
fmaster = open('master2.sql','w')
for student in students.split(','):
    fmaster.write("CREATE DATABASE %sCustomer\nGO\n" % student)
fmaster.write("\n\n")
for student in sorted(students.split(',')):
    fmaster.write("CREATE USER %s FOR LOGIN %s;\nGO\n" % (student,student))
    fmaster.write("GRANT CREATE TABLE TO %s;\n" % student)
    fmaster.write("EXEC sp_addrolemember N\'db_owner\', N\'%s\'\n\n" % student)
fmaster.close()

print("done")
