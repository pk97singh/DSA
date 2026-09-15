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
