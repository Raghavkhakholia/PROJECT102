import os
import shutil

from_dir= "C:/Users/ragha/Downloads"
to_dir = "C:/Users/ragha/OneDrive/Desktop/PYTHON/102/document_files"

list_of_files = os.listdir(from_dir)

for filename in list_of_files:
    name,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.txt', '.docx', '.doc', '.pdf']:
        path1 = from_dir + '/' + filename                             
        path2 = to_dir + '/' + "document_files"      
        path3 = to_dir + '/' + "document_files" + '/' + filename   
        
        if os.path.exists(path2):
          print("Moving " + filename + ".....")
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + filename + ".....")
          shutil.move(path1, path3)
