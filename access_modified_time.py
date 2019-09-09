import os
import time
s=os.stat(r'C:\Users\Sai\Documents\class_assignment\csv_file_handling.py')
print(time.ctime(s.st_atime))# access time
print(time.ctime(s.st_mtime))# access time
