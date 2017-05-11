def findstr(s,S):
    count = 0
    length = len(S)
    if S.find(s) == -1:
        print("not in target str")
    else:
        for each in range(length-1):
            if S[each] == s[0] and S[each+1] == s[1]:
                count += 1
    print("times = %d"%count)
    #print(count)
# s = input("sub str, length is 2")
# S = input("target str")

findstr('12','12365412789')
            
        
    
 
#返回结果是2times
        
