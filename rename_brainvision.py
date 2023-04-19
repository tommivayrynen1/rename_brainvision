
import os, fileinput
import numpy as np

# Specify folder with .dat and meta-files
folder = '/home/tvayryne/bva_rename/'

# Loop through all files
datlist=[]
flist = sorted(os.listdir(folder))
for f in flist:
    t = ".dat" in f
    if t == True:
        datlist.append(f)
    

for ind,filename in enumerate(datlist,start=1):
    print(ind)
    filebase, filetype = os.path.splitext(filename)

    # Generate new name
    newname = 'ID'+str(ind)+'_'+ filebase # 'id1' + filename
    print(newname)
    
    # Actually rename file
    os.rename(folder+filename,folder+newname+'.dat')
    os.rename(folder+filebase+'.vhdr',folder+newname+'.vhdr')
    os.rename(folder+filebase+'.vmrk',folder+newname+'.vmrk')



    for line in fileinput.FileInput(folder+newname+'.vhdr', inplace=1):
        # For header-files and marker-files
        if 'DataFile=' in line: line = 'DataFile='+newname+'.dat'
        
        # For header-files
        elif 'MarkerFile=' in line:
            line = 'MarkerFile='+newname+'.vmrk'
        print(line.replace('\n',''))


    for line in fileinput.FileInput(folder+newname+'.vmrk', inplace=1):
        if 'DataFile=' in line: line = 'DataFile='+newname+'.dat'
        print(line.replace('\n',''))
