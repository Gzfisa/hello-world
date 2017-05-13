import os
def serch_file(path,file):
    
    for each in os.listdir(path):
        if each == file:
            print(os.getcwd() + os.sep + each)
        if os.path.isdir(each):
            serch_file(path,file)
            os.chdir(os.pardir)
            
path = input('pls input path')
file = input('pls input file name')
serch_file(path,file)