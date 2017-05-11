def rep_word(file,old_word,new_word):
    f = open(file)
    
    count = 0
    content = []
    
    for eachline in f:
        count += eachline.count(old_word)
        eachline = eachline.replace(old_word,new_word)
        content.append(eachline)
    
    decide = input("%s has appeared %s times, will u replace it by %s,Yes or No?" %(old_word,count,new_word))
    
    if decide == 'Yes':
        f = open(file,"w")
        f.writelines(content)
        f.close()
    
file = "C:\\Users\\Administrator\\Desktop\\bbb.txt"
old_word = input('pls input the word u want to replace')
new_word = input('pls input the word u want to replaced by')
    
rep_word(file,old_word,new_word)
