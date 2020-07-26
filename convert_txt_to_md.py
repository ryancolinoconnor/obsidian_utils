import shutil
import glob
import os
source = "/mnt/c/Users/ryano/Google Drive/Obsidian/Big_vault/Ryan's Brain/jot notes"
files = glob.glob(os.path.sep.join([source,'*.txt']))
for f in files:
    
    outF = open(f,"r+")
    data = outF.read()
    #outF.write(data)
    outF.write('[[{date}]]'.format(date=f.split(os.path.sep)[-1].split('_')[0]))
    outF.write('[[jot_capture]]')
    outF.close()
    shutil.move(f,f.replace('.txt','.md'))