
def uniqueChars(string):
    
    s = list(string)
    ans = []
    
    dict = {}
    for i in s:
        dict[i] = dict.get(i, 0) + 1
        
        
    for i in dict:
        if dict[i]!= 1:
            dict[i]= 1 
        
    for i in s:
        if dict[i] == 1:
            ans.append(i)
            dict[i]= 0 
    print("".join(ans))
        
    

# Main
string = input()
uniqueChars(string)
