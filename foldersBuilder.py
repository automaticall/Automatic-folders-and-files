#coding utf:8
'''
useful to create file in some folder  
                        data: 03 monday 2022
@author EDJINEDJA
'''
import os 
import glob

#Build New Folder



class folder_():
    def __init__(self,link,new_folder):
        self.new_folder=new_folder
        self.link=link
        self.linkFile=self.link+'/'+self.new_folder

    def newFilenewFolder_(self):

        if not os.path.isdir(self.linkFile):
            os.makedirs(self.linkFile)


#Build New file

class file_(folder_):
    
    def __init__(self,link,new_folder,new_file):
        self.new_file=new_file
        folder_.__init__(self,link,new_folder)
        self.File__=self.linkFile+'/'+self.new_file

    def newFile_(self):

        if not os.path.isfile(self.File__):
            open(self.File__,'w')

#FOLDERS

source='C:/Users/33605/Desktop/IA'
namenewFolder='mainfolder'
folder__=folder_(source,namenewFolder)
folder__.newFilenewFolder_()

# # FILES

namenewFile='main1.py'

main_file=file_(source,namenewFolder,namenewFile)
main_file.newFile_()


#list all files .py 

listAllFiles=[i for i in glob.glob('*.py')]

print(listAllFiles)