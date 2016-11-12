''' first way '''
import os
path = "/Users/zhouke/Documents/python/src/action/src-ten/Chapter14"
i = 0
for file in os.listdir(path):
    print (file)
    if os.path.isfile(os.path.join(path,file))==True:
      
       newname='Chapter14-'+ str(i) + '.py'
       print (newname)
      
       os.rename(os.path.join(path,file),os.path.join(path,newname))
       i += 1

            


		
''' second way '''
'''
import os
import glob

path = "C://Python34//"
for infile in glob.glob( os.path.join(path, '*.gif') ):
	for i in range (1,21):
		index_symbol = "_" + str(i) + "_"
		if index_symbol in infile:
			newfile = infile
			newfile = newfile.replace(index_symbol, str(i));
			os.rename(infile, newfile)
			print (infile) 
'''
