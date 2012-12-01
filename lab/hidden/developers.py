#!/usr/bin/python2.6

# This is the web page for "developers" to upload new webpages to include in the web site
# Our web administrator is tyrannical and likes to add things himself, so he tells everyone
# to upload onto this page

import cgi
import cgitb
from upload import FileUpload
from os import path

cgitb.enable() # For now

# This file stores the name and timestamp of uploaded files
uploadsDir = "/var/www/hidden/files"
uploadsFile = "/var/www/hidden/files/uploaded.txt"

# Get the CGI info for the current file
form = cgi.FieldStorage()

# Instantiate our file upload object
uploader = FileUpload(uploadsDir, uploadsFile)

print "Content-type: text/html\n"

print """
<html>

<head><title>Developer Upload Page</title></head>

<body>

	<h1> Developers </h1>
Because we have not yet set up our source repository, we are currently allowing patches and new pages <br>
to be added to the webpage via this upload form.  Please submit all files on this page, and we will <br>
promptly update them on our directory.  Below, we also list all of the uploaded files and the time at <br>	
which they were uploaded.  Keep in mind we only keep 10 files stored at a given time.  Happy coding! 
<br>
<hr noshade size = 3>

<!-- The file upload segment -->

<form enctype="multipart/form-data" action="developers.py" method="post">
	<p>File: <input type="file" name="file"></p>
	<p><input type="submit" value="Upload"></p>
</form>

<br>
<hr noshade size = 3>
"""
if "file" in form:
	# Check that the file was properly uploaded
	uploadedFile = form["file"]
	if uploadedFile.filename:  # File exists
		# Upload the file
		uploader.upload(uploadedFile)
		print "<h2> Thanks for submitting {0}! </h2><br>".format(uploadedFile.filename)
	else:
		print "<h2> Error uploading file!"

	print "<hr noshade size = 3>"


print "<h3> Current Files </h3>"
print "<table border=1>"
# Here, I fill in the files which already exist in the file directory
savedFiles = uploader.query()
for file in savedFiles:
	# Each line has two parts, the file name and the timestamp, so print all of the files out here
	name = file[0]
	time = file[1]
	print "<tr><td>{0}</td><td>{1}</td></tr>".format(name, time)

print """
</table>
<br>
<br>
<footer>
	<hr noshade size = 3>
	<p>Created by: The SUPER SECURITY team</p>
</footer>
"""