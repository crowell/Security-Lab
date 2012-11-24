# Simple class for uploading and saving the files in the proper directorys
"""Module for file upload

Contains a single class, FileUpload, which is used to upload files to a given directory
when using basic python CGI
"""

from os import listdir, remove, rename
import datetime

class FileUpload(object):
	"""Upload, delete, and query files uploaded to files directory"""

	MAXFILES = 10

	def __init__(self, direct, ln):
		""" Instantiation, takes two arguments

		direct - The directory of the uploaded files
		ln - The name of the text file which will contain timestamps and filenames
		"""
		super(FileUpload, self).__init__()
		self.directory = string.rstrip(direct, '/') # strip end slash if it exists
		self.filelist = ln  

	def upload(fileitem):
		""" Uploads a file and saves name and timestamps

		fileitem - the file item returned from CGI script uploads
		"""
		# First check to see if max files has been reached, and if so, delete oldest
		files = self.query()
		if (len(files) >= MAXFILES):
			self.delete()

		# Save the new file into the directory and filelist
		fileContents = fileitem.file.read()
		filename = os.path.basename(fileitem.filename)
		h = open(self.directory + '/' + filename, 'wb')
		h.write(fileContents)
		h.close()

		# Save a filename and timestamp to the file
		self.addToList(filename)


	def delete():
		""" Deletes the top most file in filelist from the directory 

		Also removes the file from the filelist.  This makes the filelist txt file operate very similarly
		to a permanent stored queue
		"""
		files = self.query()
		if len(files) not 0:
			os.remove(self.directory + '/' + files[0][0]) # Remove topmost file
			self.removeTop()


	def query():
		""" Query the filelist and return all files and timestamps in a list"""
		with open(self.filelist, 'r') as list:
			lines = list.readlines();
			for line in lines:
				line.split('\t')

		return lines


	def addToList(filename):
		""" Adds filename into the filelist and gives a timestamp """
		with open(self.filelist, 'a') as list:
			time = datetime.datetime.now()

			list.write(filename + "\t" + time)

	def removeTop():
		""" Removes top file from filelist """
		with open(self.filelist, 'rw') as inp:
			with open(self.filelist+'_NEW', 'rw') as out:
				original = inp.readlines()
				new = original[1:]
				out.writelines(new)

		os.remove(self.filelist)
		os.rename(self.filelist+'_NEW', self.filelist)


