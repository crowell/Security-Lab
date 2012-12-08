# Chmod all of the hidden CGI files
chmod 777 hidden/developers.py hidden/dev_login.py hidden/upload.py

# Make sure the files directory exists
cd hidden/files
rm -f *
cd ../..

chmod 777 -R data/
chmod 775 ssi/response.py
chmod a+r -R ssi