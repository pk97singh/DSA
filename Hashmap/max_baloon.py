def max_baloon(s1):
    s="baloon"
    n=len(s)
    dict={}
    count=float('inf')
    if len(s1)>len(s):
        
        for char in s1:
                dict[char]=dict.get(char,0)+1
                
        
    for char in s:
        if char not in dict:
            return 0
        
        print('count',count)
        print('dict char',char,dict[char])
        print('s.count char',s.count(char))
        count = min(count, dict[char] // s.count(char))
     
    
    return count
    
    
ip="loonbalxballpoon"
print(max_baloon(ip))
