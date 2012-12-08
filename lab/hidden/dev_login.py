#!/usr/bin/python2.6

# Login page for the developer portal

import cgi
import os
import cgitb
import Cookie
import datetime
import random
cgitb.enable()

# My different possible page
def redirect(cookie):
	print cookie
	print "Status: 301"
	print "Location: developers.py"
	print "Content-Type: text/html\n"

def printFail(cookie):
	cookie['username'] = ""
	print cookie
	print "Status: 403"
	print "Content-Type: text/html\n"
	print "<h1>403 Forbidden</h1>"

def printPage(cookie):
	print cookie
	print "Content-Type: text/html\n"
	print """
<html>
<h1>Developer Page Login</h1>
<body>
"""
	print """
	<form action=dev_login.py method=post>
		<table border="0"> 
			<tr><td colspan=2><h1>Login</h1></td></tr> 
			<tr><td>Username:</td><td> 
			<input type="text" name="username" maxlength="40"> 
			</td></tr> 
			<tr><td>Password:</td><td> 
			<input type="password" name="password" maxlength="50"> 
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
		cookie['username'] = form['username'].value
		cookie['password'] = form['password'].value
	else:
		# No submission, or messed up submission
		cookie['username'] = oldCookie[0]
		cookie['password'] = oldCookie[1]
except:
	# No previous values
	cookie['username'] = ""
	cookie['password'] = ""

#update cookie expiration date
expirationDate = datetime.datetime.now() + datetime.timedelta(hours = 24)
cookie['username']['expires'] = expirationDate.strftime('%a, %d %b %Y %H:%M:%S')
cookie['whoami'] = "Login Credentials"

# Finally, print the cookie
if cookie['username'].value == "admin" and cookie['password'].value == "letmein":
	# redirect to the developers page
	redirect(cookie)
else:
	# Now, see what's in the cookie, that will decide which page to go to
	if cookie['username'].value != "":
		# Print this page with a fail login message
		printFail(cookie)
	else:
		# Print the page normally
		printPage(cookie)