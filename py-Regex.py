#pyregex - a program that opens all txt files in a folder and searched for a
#user supplied regex within that txt file.



import os, re

userSearch = input('Enter text to search:\n')   



for folderName, subfolders, filenames in os.walk(os.getcwd()):      
        for filez in filenames:        
            
            if filez.endswith('.txt'):              
                currentFiles = open(filez, 'r')     
                fileRead = currentFiles.read()      

                txtSearch = re.compile(userSearch)          #searches for what the user inputed
                reResult = txtSearch.search(fileRead)

                if reResult == None:            # if result is not found, restart the loop
                    continue

                print(reResult.group())         
                print('Text found in ' + filez)                    #prints what file the text was found in









        
       
            

