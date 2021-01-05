from pathlib import Path
import os
path=Path.cwd()
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if os.path.getsize(str(Path(foldername, filename)))>100000000: #100 MB 
            print("The size of  %s is %s "%(Path(foldername,filename),os.path.getsize(str(Path(foldername, filename)))))
