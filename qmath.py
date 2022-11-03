#                                           qmath.py
#collection of scratch made code snippets, loosely secured, open-accessed and reusable modular fns 
#                               Pertaining to quadratic equations and solving them
#                                           by: Sinefyre
#__________________________________________________________________________________________________#

import math, cmath #math for math stuff like sqrt, cmath to handle unreal solutions

#-----------------------------------------
#this function, given coefs aka 3 ints, is the quadratic equation, it solves it and returns solutions
#-----------------------------------------
def qfrm(a,b,c): #any variable or function can be callable from a module to wherever though, vars w/in a fn only persists WITHIN the containing fns scope
    
    discrim = math.pow(b,2)-4*a*c #Get the discriminant

    if(discrim<0):  #condition when Discrim is neg, implication of  unreal solutions, use of cmath fn to handle it
        x1= (-b+(cmath.sqrt(discrim)))/(2*a)
        x2= (-b-(cmath.sqrt(discrim)))/(2*a)
    elif(discrim>=0): #condition when Discrim is pos, implication of real solutions, use of regular math fn
        x1= (-b+math.sqrt(discrim))/(2*a)
        x2= (-b-math.sqrt(discrim))/(2*a)
       
    sol_set = (x1,x2) #is a tuple here , can be converted outside to any other collection type
    return sol_set

#-----------------------------------------
#this function, given coefs aka 3 ints, returns y-intercept value; (0,y)
#-----------------------------------------
def qyint(a,b,c):
    x=0
    y = (a*x**2)+(b*x)+c
    return y

#-----------------------------------------
#this function, given coefs aka 3 ints, returns h value of the vertex point; of  (h,k)
#-----------------------------------------
def vertex_h(a,b,c):
    h = -b/(2*a)
    return h

#-----------------------------------------
#this function, given coefs aka 3 ints, returns the k value of the vertex point; of (h,k)
#-----------------------------------------
def vertex_k(a,b,c):
    h =  vertex_h(a,b,c)
    y = (a*h**2)+(b*h)+c #x = h, algebraic connection
    return y

#-----------------------------------------
#this function, given coefs aka 3 ints, returns as a 2-item tuple, the point (h,k)
#-----------------------------------------
def vertex_point(a,b,c):
    return (vertex_h(a,b,c), vertex_k(a,b,c)) 

#-----------------------------------------
#this function, given an int (Which is the a val and its sign alg)returns as a string whether a given quadratic opens up/down and has either min/max 
#-----------------------------------------
def qorient(a):
    if(a<0):
        return "Open Down; w/ Maxima"
    else:
        return "Open Up; w/ Minima"

#-----------------------------------------
#this function, given coefs aka 3 ints, and 1 int (k of vertex) returns if min or max, redundant, 11/02/2022 -> Will remove some time after date
#-----------------------------------------
def min_or_max(a,b,c,k):
    k = vertex_k(a,b,c)
    if(a<0):
        return "STATE: minima"
    elif(a>0):
        return "STATE: maxima"
    
    
#____________________________________________________________________#
if __name__ == '__main__':
    pass