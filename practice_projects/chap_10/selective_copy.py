import os,shutil
from pathlib import Path
folder=Path.cwd()
#final_destination=Path.home()/Path('dumpster')
for foldername, subfolders, filenames in os.walk(folder):
    for files in filenames:
        if files.endswith('.txt') or files.endswith('.py'):
            print("Copying the file %s in %s folder to '/home/akki/dumpster'"%(files,foldername))
            shutil.copy(foldername/Path(files),Path('/home/akki/dumpster')) # copy, be veryyyy careful with move for copying
            print("Copied the file %s in '/home/akki/dumpster/%s'"%(files,files) )
