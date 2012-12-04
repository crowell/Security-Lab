# Simple class for uploading and saving the files in the proper directorys
"""Module for file upload

Contains a single class, FileUpload, which is used to upload files to a given directory
when using basic python CGI
"""

from os import listdir, remove, rename, path, chmod
import datetime
import string

class FileUpload(object):
	"""Upload, delete, and query files uploaded to files directory"""

	def __init__(self, direct, ln):
		""" Instantiation, takes two arguments

		direct - The directory of the uploaded files
		ln - The name of the text file which will contain timestamps and filenames
		"""
		super(FileUpload, self).__init__()
		self.directory = string.rstrip(direct, '/') # strip end slash if it exists
		self.filelist = ln  
		self.MAXFILES = 10;

	def upload(self, fileitem):
		""" Uploads a file and saves name and timestamps

		fileitem - the file item returned from CGI script uploads
		"""

		files = self.query()

		# First check to see if the file exists already or they are trying to upload a bad file
		for ii, file in enumerate(files):
			if fileitem.filename == file[0]:
				# We have to remove this file from the list in order to properly reload it
				# Note that we dont have to delete the file since it will be overwritten
				self.removeFileAtIndex(ii)

			if fileitem.filename == "uploaded.txt":
				# We do not want to let users alter the uploaded.txt file
				return -1

		# Then check to see if max files has been reached, and if so, delete oldest
		if (len(files) >= self.MAXFILES):
			self.delete()

		# Save the new file into the directory and filelist
		fileContents = fileitem.file.read()
		filename = path.basename(fileitem.filename)
		h = open(self.directory + '/' + filename, 'w')
		chmod(self.directory + "/" + fileitem.filename, 0777);
		h.write(fileContents)
		h.close()		

		# Save a filename and timestamp to the file
		self.addToList(filename)
		return 0


	def delete(self):
		""" Deletes the top most file in filelist from the directory 

		Also removes the file from the filelist.  This makes the filelist txt file operate very similarly
		to a permanent stored queue
		"""
		files = self.query()
		if len(files) != 0:
			remove(self.directory + '/' + files[0][0]) # Remove topmost file
			self.removeFileAtIndex(0)


	def query(self):
		""" Query the filelist and return all files and timestamps in a list"""
		filelist = []
		try:
			with open(self.filelist, 'r') as list:
				lines = list.readlines();
				for line in lines:
					filelist.append(line.split('\t'))
		except IOError:
			# File does not exist, so create it and return an empty list
			filelist = []

		return filelist


	def addToList(self, filename):
		""" Adds filename into the filelist and gives a timestamp """
		with open(self.filelist, 'a+') as list:
			time = datetime.datetime.now()

			list.write(filename + "	" + str(time) + "\n")
		# Make sure permissions are correct on uploaded.txt
		chmod(self.filelist, 0777);

	def removeFileAtIndex(self, index):
		""" Removes top file from filelist """
		try:
			with open(self.filelist, 'rw') as inp:
				with open(self.filelist+'_NEW', 'w') as out:
					lines = inp.readlines();
					for ii, line in enumerate(lines):
						if ii != index:
							# Only copy line if it is not being removed
							out.writelines(line)
			remove(self.filelist)
			rename(self.filelist+'_NEW', self.filelist)
		except IOError:
			# Empty file, so just leave it be
			print "No files found"



