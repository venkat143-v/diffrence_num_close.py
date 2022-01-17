def test(a,b): 
 diff=a-b 
 if(diff<=0.001): 
 return(diff,'close') 
 else: 
 return(diff,'not close') 
a=float(input('a=')) 
b=float(input('b=')) 
k=test(a,b) 
print(k) 
