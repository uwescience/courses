import sys
import os


# files

## file with usernames and & codes
infilename = sys.argv[1]

## location to create directories
inlocationname = sys.argv[2]

dirname = inlocationname

if not os.path.isdir("./" + dirname + "/"):
	os.mkdir("./" + dirname + "/")

# Get the users
infile = open(infilename,"r")
while infile:
	line = infile.readline()
	line = line.strip()

	if len(line)==0:
		break

	entries = line.split(",")

	# parse the important info
	firstname = entries[1].replace("\"","").strip()
	lastname = entries[0].replace("\"","").strip()
	username = entries[2].replace("\"","").strip()
	code =  entries[3].replace("\"","").strip()
	
	
	# create directory
	userdir = "./" + dirname + "/" + username + "/"
	os.mkdir(userdir)

	# create code webpage
	webpagehtml = "<html><body>"
	webpagehtml = webpagehtml + "<h1> Welcome "+ firstname +" "+ lastname+"</h1> <br>"
	webpagehtml = webpagehtml + " <p> Your Amazon AWS code for Spring 2011 will be:</p> <br>"
	webpagehtml = webpagehtml + code +" <br>"
	webpagehtml = webpagehtml + "</body></html>"

	OUTPUTFILE = open(userdir+"index.html", "w")
	OUTPUTFILE.write(webpagehtml)
	OUTPUTFILE.close()

	# create security file
	securtityhtml = "authtype csenetid\n"
  	securtityhtml =	securtityhtml +	"authname \"CSE344 Spring 2011 AWS Codes\"\n"
  	securtityhtml = securtityhtml + "require user "+username+"\n"

	OUTPUTFILE = open(userdir+".htaccess", "w")
	OUTPUTFILE.write(securtityhtml)
	OUTPUTFILE.close()
		
	if len(line)==0:
		break


