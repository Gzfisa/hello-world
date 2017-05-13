import os
def serch_file(path,vedio_ext):
    os.chdir(path)
    vedio_list = []
    for each in os.listdir(os.curdir):
        ext = os.path.splitext(each)[1]
        
        if ext in vedio_ext:
            vedio_list.append(os.getcwd() + os.sep + each + os.linesep)
            
        if os.path.isdir(each):
            serch_file(path,vedio_ext)
            os.chdir(os.pardir)

vedio_ext = ['.avi','.rmvb','.mp4']
path = input('pls input path')            
vedio_dir = os.getcwd()

serch_file(path,vedio_ext)

f = open(vedio_dir + os.sep + 'vedio.txt','w')
f.writelines(vedio_list)
f.close()