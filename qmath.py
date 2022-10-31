import math, cmath
def qfrm(a,b,c): #any variable or function can be callable from a module to wherever though, vars w/in a fn only persists WITHIN the containing fns scope
    
    discrim = math.pow(b,2)-4*a*c

    if(discrim<0):  #condition when Discrim is neg
        x1= (-b+(cmath.sqrt(discrim)))/(2*a)
        x2= (-b-(cmath.sqrt(discrim)))/(2*a)
    elif(discrim>=0): #condition when Discrim is pos
        x1= (-b+math.sqrt(discrim))/(2*a)
        x2= (-b-math.sqrt(discrim))/(2*a)
       
    sol_set = (x1,x2)
    return sol_set
    
def qyint(a,b,c):
    x=0
    y = (a*x**2)+(b*x)+c
    return y

def vertex_h(a,b,c):
    h = -b/(2*a)
    return h

def vertex_k(a,b,c):
    h =  vertex_h(a,b,c)
    y = (a*h**2)+(b*h)+c #x = h
    return y
    
def vertex_point(a,b,c):
    return (vertex_h(a,b,c), vertex_k(a,b,c)) 
    
def qorient(a):
    if(a<0):
        return "Open Down; w/ Maxima"
    else:
        return "Open Up; w/ Minima"
        
def min_or_max(a,b,c,k):
    k = vertex_k(a,b,c)
    if(a<0):
        return "STATE: minima"
    elif(a>0):
        return "STATE: maxima"
    
    
#note python files have special attributes of themselves, to a files perspective it's always main
if __name__ == '__main__':
    print(qfrm(6,7,-3))
    print("Is as __main__")