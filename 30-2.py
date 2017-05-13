import os
def file_size(path):
    
    file_dic = dict()
    
    for each in os.listdir(path):
        if os.path.isfile(each):
            size = os.path.getsize(each)
            file_dic[each] = size
        if os.path.isdir(each):
            file_size(path)
            os.chdir(os.pardir)

    for each_item in file_dic.items():
        print('%s,[%dBytes]' %(each_item[0],each_item[1]))   
   
path = input('pls input the path u want to search')
file_size(path)      