#!/usr/bin/python2.6
import cgi
import cgitb
cgitb.enable()

print "Content-type: text/html\n"
print ""
form = cgi.FieldStorage()
pluginName = form["pluginName"].value.lower()

print """
<html>
<head>
<title>SSI Test Page</title>
</head>
<body>
<p>Here's more information about the plugin your searched for.</p>
</body>
</html>
"""

def blindsqli():
	print "<b>%s</b></br></br>"%pluginName
	print """
<html>
This plugin finds blind SQL injections.</br></br>
Two configurable parameters exist:</br>
&nbsp;&nbsp;&nbsp;&nbsp;- equAlgorithm</br>
&nbsp;&nbsp;&nbsp;&nbsp;- qualLimit</br></br>
The equAlgorithm parameter configures how the comparison of pages is done, the options for equAlgorithm are:</br>
&nbsp;&nbsp;&nbsp;&nbsp;- stringEq</br>
&nbsp;&nbsp;&nbsp;&nbsp;- setIntersection</br></br>
The classic way of matching two strings is "stringEq" , in Python this is "string1 == string2" , but other ways have been developed for sites that have changing banners and random data on their HTML response. "setIntersection" will create two different sets with the words inside the two HTML responses, and do an intersection. If number of words that are in the intersection set divided by the total words are more than "equalLimit", then the responses are equal.
</html>
"""

def ssi():
	print "<b>%s</b></br></br>"%pluginName
	print """
<html>
This plugin finds server side include (SSI) vulnerabilities.
</html>
"""

def fileupload():
	print "<b>%s</b></br></br>"%pluginName
	print """
<html>
This plugin will try to exploit insecure file upload forms.</br></br>
One configurable parameter exists:</br>
&nbsp;&nbsp;&nbsp;&nbsp;- extension</br></br>
The extensions parameter is a comma separated list of extensions that this plugin will try to upload. Many web applications verify the extension of the file being uploaded, if special extensions are required, they can be added here.</br></br>
Some web applications check the contents of the files being uploaded to see if they are really what their extension is telling. To bypass this check, this plugin uses file templates located at "plugins/audit/fileUpload/", this templates are valid files for each extension that have a section ( the comment field in a gif file for example ) that can be replaced by scripting code ( PHP, ASP, etc ).</br></br>
After uploading the file, this plugin will try to find it on common directories like "upload" and "files" on every know directory. If the file is found, a vulnerability exists. 
</html>
"""

def xss():
	print "<b>%s</b></br></br>"%pluginName
	print """
<html>
This plugin finds Cross Site Scripting (XSS) vulnerabilities.</br></br>
Two configurable parameters exist:</br>
&nbsp;&nbsp;&nbsp;&nbsp;- checkStored</br>
&nbsp;&nbsp;&nbsp;&nbsp;- numberOfChecks</br></br>
To find XSS bugs the plugin will send a set of javascript strings to every parameter, and search for that input in the response. The parameter "checkStored" configures the plugin to store all data sent to the web application and at the end, request all pages again searching for that input; the numberOfChecks determines how many javascript strings are sent to every injection point.
</html>
"""

def webspider():
	print "<b>%s</b></br></br>"%pluginName
	print """
<html>
This plugin is a classic web spider, it will request a URL and extract all links and forms from the response.</br></br>
Four configurable parameters exist:</br>
&nbsp;&nbsp;&nbsp;&nbsp;- onlyForward</br>
&nbsp;&nbsp;&nbsp;&nbsp;- ignoreRegex</br>
&nbsp;&nbsp;&nbsp;&nbsp;- followRegex</br>
&nbsp;&nbsp;&nbsp;&nbsp;- urlParameter</br></br>
IgnoreRegex and followRegex are commonly used to configure the webSpider to spider all URLs except the "logout" or some other more exciting link like "Reboot Appliance" that would make the w3af run finish without the expected result.</br></br>
By default ignoreRegex is 'None' (nothing is ignored) and followRegex is '.*' ( everything is followed ). Both regular expressions are normal regular expressions that are compiled with the python's re module.
</html>
"""

options = {'blindsqli' : blindsqli,
		'ssi' : ssi,
		'server side include' : ssi,
		'fileupload' : fileupload,
		'file upload' : fileupload,
		'xss' : xss,
		'cross site scripting' : xss,
		'cross-site scripting' : xss,
		'webspider' : webspider,
		'web spider' : webspider,
}


try :
	options[pluginName]()
except :
	var = '<!--#include file="/etc/passwd"-->'
	if pluginName == var:
		pluginName = '<!--#include file="etc/passwd"-->'

	print "Sorry, our lab does not focus on the use of the following plugin:</br></br>"

	print "%s" % pluginName
