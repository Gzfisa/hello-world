def type_found(path):

    import os
    l =  os.listdir(path)
    type_num = dict()
    
    for each in l:
        if os.path.isdir(each):
            type_num.setdefault('file',0)
            type_num['file'] += 1
        else:
            ext = os.path.splitext(each)[1]
            type_num.setdefault(ext,0)
            type_num[ext] += 1
            
    for each_type in type_num.keys():
        print('The number of %s is %d'(ext,type_num[each_type]))

# path = input('pls input the path u want to check')

type_found(path)