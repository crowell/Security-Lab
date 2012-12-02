#!/usr/bin/python2.6

# Login page for the developer portal

import cgi
import os
import cgitb
import Cookie
cgitb.enable()

# My different possible pages
def redirect():
	print "Status: 301 moved"
	print "Location: developers.py"

def printPage(attempt):
	print "Content-type: text/html\n"

	print """
<html>
<h1>Developer Page Login</h1>
<body>
"""
	if attempt:
		print "Login failed, try again<br>"

	print """
	<form action=dev_login.py method=post>
		<table border="0"> 
			<tr><td colspan=2><h1>Login</h1></td></tr> 
			<tr><td>Username:</td><td> 
			<input type="text" name="username" maxlength="40"> 
			</td></tr> 
			<tr><td>Password:</td><td> 
			<input type="password" name="pass" maxlength="50"> 
			</td></tr> 
			<tr><td colspan="2" align="right"> 
			<input type="submit" name="submit" value="Login"> 
			</td></tr> 
		</table> 
	</form> 
</body>
</html>
"""




## MAIN PART OF PAGE ##

# Get the recent form info
form = cgi.FieldStorage()

# Get the cookie
try:
	cookie = Cookie.SimpleCookie()
	cookie.load(os.environ["HTTP_COOKIE"])
except:
	cookie = Cookie.SimpleCookie()

# First try to update the cookies
try:
	oldCookie = []
	oldCookie.append(cookie['username'].value)
	oldCookie.append(cookie['password'].value)
	if 'username' in form:
		# Form was submitted 
		cookie['username'] = form['username']
		cookie['password'] = form['password']
	else:
		# No submission, or messed up submission
		cookie['username'] = oldCookie[0]
		cookie['password'] = oldCookie[1]
except:
	# No previous values
	cookie['username'] = None
	cookie['password'] = None

# Now, see what's in the cookie, that will decide which page to go to
if cookie['username'] not None:
	# I hard code the username here
	if cookie['username'] == "admin" and cookie['password'] == "letmein":
		# redirect to the developers page
		redirect()
	else:
		# Print this page with a fail login message
		printPage(True)
else:
	# Print the page normally
	printPage(False)