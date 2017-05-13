import os

def Key_print(key_dic):
    keybox = key_dic.keys()
    keybox = sorted(keybox)
    for each_key in keybox:
        print('Keyword is in Line %s, position %s'%(each_key,str(key_dic[each_key])))
                
def pointer_key(line,keyword):
    
    pointer = line.find(keyword)
    pointer_list = []
    while pointer != -1:
        pointer_list.append(pointer+1) 
        pointer = line.find(keyword, pointer+1)
    return pointer_list
                
def keyword_dic(file_txt,keyword):
    count = 0
    key_dic = dict()
    file = open(file_txt)        
    for each_line in file:
        count += 1
        if keyword in each_line:
            pointer_keyword = pointer_key(each_line,keyword)
            key_dic[count] = pointer_keyword
    file.close()
    return key_dic            
        
def txtfile_search(keyword,decide):
    
    temp = os.walk(os.getcwd())
    txtfile = []
    for each_tuple in temp:
        for each_file in each_tuple[2]:
            if os.path.splitext(each_file) == '.txt':
                txtfile.append(os.path.join(each_tuple[0],each_file))
                for each_file in txtfile:
                    key_dic = keyword_dic(each_file,keyword)
                    if key_dic:
                        print('=====================================')
                        print('In %s found %s' %(each_file,keyword))
                        if decide in ['YES','Yes','yes']:
                            Key_print(key_dic)      

    
keyword = input('pls put this script program in the file u need to search, and input the keyword u want to search for')
decide = input('Do u need to print the position of %s in the text?Pls input[Yes or No]')
txtfile_search(keyword,decide)
    
    