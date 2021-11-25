import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

drive_folder_id=os.environ.get('DRIVE_FOLDER_ID')

def upload_file(file_path):
  print("uploading file")
  # gfile = drive.CreateFile({"parents": [{"id": drive_folder_id}]})
  # print(gfile)
  # print(file_path)
  # gfile.SetContentFile(file_path)
  # print(gfile)
  # gfile.Upload()
  file1 = drive.CreateFile({"title": "Hello.txt"})
  print(file1)
  file1.Upload()
  print("file successfully uploaded")
  return file1['id']
