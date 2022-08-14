# Documentation -- https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
