#check valid brackets
s1="{[()]}"
stack=[]
for ch in s1:
    if ch in "{([":
        stack.append(ch)
        continue
    if not stack:
        print("false")
        break
            
    top=stack[-1]
    if ((ch =="}" and top !="{" ) or 
       (ch ==")" and top !="(" ) or 
       (ch =="]" and top !="[" )):
           print("false")
           break
           
    stack.pop()
    
if len(stack)==0:
        print("true")

#decode
def decode(s1):
    stack=[]
    current=""
    num=0 
    for ch in s1:
        if ch.isdigit():
            num=num*10+int(ch)
        
        elif ch=='[':
            stack.append((current,num))
            current=""
            num=0
            
        elif ch==']':
            prev,count=stack.pop()
            current=prev+current*count 

            
        else:
            current+=ch
            
    return current 


print(decode("3[a2[b]]"))

#circular array 
def cicular_arr(arr1):
    n=len(arr1)
    stack=[]
    res=[-1]*n
    for i in range(n*2-1,-1,-1):
        while stack and stack[-1]<=arr1[i%n]:
            stack.pop()
            
        if i<n:
            if stack:
                res[i]=stack[-1]
                
        stack.append(arr1[i%n]) 
        
    return res

print(cicular_arr([1, 2, 3, 4, 3]))

