import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

drive_folder_id=os.environ.get('DRIVE_FOLDER_ID')

def upload_file(file_path):
  gfile = drive.CreateFile({'parents': [{'id': drive_folder_id}]})
  gfile.SetContentFile(file_path)
  gfile.Upload()
  return gfile['id']
