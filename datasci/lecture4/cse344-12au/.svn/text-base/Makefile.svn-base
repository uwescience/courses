# --------------------------------------------------
# Variables used in the script
# --------------------------------------------------
# TODO
#
# 1) Update the environment variable STAGE_DIR and PUBLIC_DIR below
#
# 2) At the beginning of the quarter, set HOMEWORKS to the empty string
# HOMEWORKS =
# Then, as you want to publish each assignment, add the assignment to the list
# HOMEWORKS = hw1
# HOMEWORKS = hw1 hw2
# etc.
# 
# HOW TO USE THE MAKEFILE
# The goal of the makefile is to automatically populate the course website
# from a local check-out of the svn repository. Simply run:
# make public
#
# Before making changes public, to play test them in a staging area run:
# make stage. See PUBLIC_DIR and STAGE_DIR for the location of the 
# course website and staging area.
#
# See "help" below for more details.
#
# SOME DETAILS
# 
# The makefile primarily copies everything from under "html" to the
# course website at PUBLIC_DIR.
# For the assignments, the makefile picks everything up from the
# assignments directory (instructions and addtional files) and copies over 
# what it needs into the html directory. EXCEPT for solutions. 
# Solutions need to be manually put into the html directory.
# The reason is that we want to avoid publishing solutions by accident.
#

#HOMEWORKS = hw1 hw2 hw3 hw4 hw5 hw6
HOMEWORKS = hw1 hw2 hw3 hw4 
SHELL = /bin/bash

GROUP = cse344
ifndef $(STAGE_DIR)
STAGE_DIR = /cse/www/education/courses/cse344/12au/stage
endif
PUBLIC_DIR = /cse/www/education/courses/cse344/12au

ifndef $(LOGIN)
	LOGIN=$(USER)
endif

ASSIGN_DIR = assignments
HTML_ASSIGN_DIR = html/hw

HOMEWORK_HTML_DIRS = ${HOMEWORKS:hw%=${HTML_ASSIGN_DIR}/hw%}

LECTURES_DIR = lectures/public/
HTML_LECTURES_DIR = html/lectures

EXAMS_DIR = exams/public/
HTML_EXAMS_DIR = html/exams

SECTIONS_DIR = sections/public/
HTML_SECTIONS_DIR = html/sections

# --------------------------------------------------

all: help

# Copy over all the instructions and additional files for one assignment
${HTML_ASSIGN_DIR}/hw%:
	echo "Got here"
	# Create the assignment dir if it doesn't already exist (we recreate it every time we build)
	mkdir -pv ${HTML_ASSIGN_DIR}/hw$*/
	# Copy over instruction files
	cp -pv ${ASSIGN_DIR}/hw$*/instructions/*.* ${HTML_ASSIGN_DIR}/hw$*/
	# Tar, zip, and copy over all additional files (3 steps)
	# Step 1: Copy all the files and directories inside additional-files (if any) into a temporary directory
	svn export ${ASSIGN_DIR}/hw$*/additional-files hw$* || echo ''
	# Step 2: Create the tar file from the temporary directory
	if [ -e hw$* ]; then tar zcvf $@/hw$*.tar.gz hw$* ; fi
	# Step 3: Remove the temporary directory
	rm -rf hw$*

help:
	@echo
	@echo 'Targets:'
	@echo '  clean - delete old assignment instructions and tar balls in the html directory.'
	@echo '  lecturenotes - copy the lectures to the html directory'
	@echo '  sectionnotes - copy the lectures to the html directory'
	@echo '  hw-dirs - make homework instruction directories'
	@echo '  stage - publish into staging directory STAGE_DIR'
	@echo '          if unset, defaults to official staging directory.'
	@echo '  stage LOGIN=username -- uses a different username for scp/ssh command'
	@echo '  public - publish into public website.'
	@echo

clean:
	rm -Rf ${HOMEWORK_HTML_DIRS} 
	rm -Rf ${PROJECT_HTML_DIRS} 

lecturenotes:
## Copy the lecture notes to the hmlt directory. 
## Using rsync instead of cp, because it's easier to exclude the .svn files
	rsync -vzrltO --exclude .svn/ ${LECTURES_DIR} ${HTML_LECTURES_DIR} || echo ''

examnotes:
## Copy the exams to the hmlt directory. Only copy .pdf
## Using rsync instead of cp, because it's easier to exclude the .svn files
	rsync -vzrltO --exclude .svn/ ${EXAMS_DIR} ${HTML_EXAMS_DIR} || echo ''

sectionnotes:
## Copy the section notes to the hmlt directory
## Using rsync instead of cp, because it's easier to exclude the .svn files
	rsync -vzrltO --exclude .svn/ ${SECTIONS_DIR} ${HTML_SECTIONS_DIR} || echo ''

hw-dirs: ${HOMEWORK_HTML_DIRS}
	echo ${HOMEWORK_HTML_DIRS}

clean-stage:
	rm -Rf ${STAGE_DIR}/*

clean-public:
	rm -Rf ${PUBLIC_DIR}/*

stage: clean 
	make lecturenotes
	make sectionnotes
	make examnotes
	make publish PUBLISH_DIR=${STAGE_DIR}

public: clean
	make lecturenotes
	make sectionnotes
	make examnotes
	make publish PUBLISH_DIR=${PUBLIC_DIR}

publish: hw-dirs 
	@cd html && rsync -vzrltO --exclude .svn/ . ${LOGIN}@barb.cs.washington.edu:${PUBLISH_DIR} || echo ''
	@ssh  ${LOGIN}@barb.cs.washington.edu  chmod -R ug+rwX,o+rX ${PUBLISH_DIR}


