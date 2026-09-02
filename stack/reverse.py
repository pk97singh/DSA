def reverse_string(s):
    stack=[]
    n=len(s)
    res=""
    
    for i in range(0,n):
        stack.append(s[i])
        
    while (stack):
        c=stack.pop()
        res+=c
        
    return res 

print(reverse_string("hello"))

# stack.append(x)   # push

# stack[-1]         # top / peek

# stack.pop()       # pop

# while stack:      # stack is not empty
