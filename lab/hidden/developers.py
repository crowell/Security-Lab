# This is the web page for "developers" to upload new webpages to include in the web site
# Our web administrator is tyrannical and likes to add things himself, so he tells everyone
# to upload onto this page

import cgi
import cgitb
import upload
from os import listdir

cgitb.enable() # For now

# This file stores the name and timestamp of uploaded files
uploadsDir = "/var/www/hidden/files"
uploadsFile = "/var/www/hidden/uploaded.txt"

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

<form enctype="multipart/form-data" action="save_file.py" method="post">
	<p>File: <input type="file" name="file"></p>
	<p><input type="submit" value="Upload"></p>
</form>

<br>
<hr noshade size = 3>
"""
if "file" in form:
	# Check that the file was properly uploaded
	uploadedFile = form["file"]
	if uploadedFile.filename:
		name = os.path.basename(uploadedFile.filename)
		print name # Just some debug info
		# Upload the file
		uploader.upload(name)
		print "<h2> Thanks for submitting {0}! <h2><br>".format(name)
	else:
		print "<h2> Error uploading file!"

print "<table>"

# Here, I fill in the files which already exist in the file directory
for file in uploader.query():
	# Each line has two parts, the file name and the timestamp, so print all of the files out here
	name = file[0]
	time = file[1]
	print "<tr><td>{0}</td><td>{1}</td></tr>".format(name, time)

print """
</table>

<footer>
	<p>Created by: The SUPER SECURITY team</p>
	<p><time pubdate datetime="2012-11-24"></time></p>
</footer>
