pnom = input("Enter orderly coefs sep'd by comma\nExample>>1,2,3,4....\n>>")
import pmath 
#print(pnom, " <-- before processing; is string")    shows it's initially a string
pnom = pmath.process_pnom(pnom)   #The fn used converts a string into a list of integers
#print(pnom, " <-- after  processing; is list of integers")  shows you done it

pnom_roots= pmath.calc_pnom_roots(pnom)
print(pnom_roots , "<-\n\n")


"""
multiplicity_set=[]
for n in range(len(pnom_roots)):
    mult_ct = 0
    temp_list = calc_pnom_quotient(pnom, pnom_roots[n])
    
    count=n
    while(count<len(pnom_roots)):
        if(temp_list[len(temp_list)-1]==0):
            mult_ct+=1
            print("realtime breakdown: ", temp_list)
        temp_list= calc_pnom_quotient(temp_list,pnom_roots[n])
        count+=1
    multiplicity_set.append(mult_ct)
        """
print(pmath.calc_multiplicities(pnom, pnom_roots), "<- are ordered multiplicities")
pholder = pmath.calc_complex_roots(pnom,pnom_roots,pmath.calc_multiplicities(pnom, pnom_roots))
print(pholder)

"""
from fractions import Fraction

actual_roots = calc_actual_rats(pnom, pnom_roots) <- how to get actual roots
actual_roots = sorted(actual_roots) #sort in ascending order  <- if you want sorted
print("Processes roots: ", actual_roots) <- prints them

"""

