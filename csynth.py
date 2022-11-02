pnom = input("Enter orderly coefs sep'd by comma\nExample>>1,2,3,4....\n>>")
import pmath 
#print(pnom, " <-- before processing; is string")    shows it's initially a string
pnom = pmath.process_pnom(pnom)   #The fn used converts a string into a list of integers
#print(pnom, " <-- after  processing; is list of integers")  shows you done it

pnom_roots= pmath.calc_pnom_roots(pnom)
print(pnom_roots , "<-polynomial roots set\n\n")


print(pmath.calc_multiplicities(pnom, pnom_roots), "<- are ordered multiplicities")

unrealzeros = pmath.stepwise_simplifier(pnom,pnom_roots,pmath.calc_multiplicities(pnom, pnom_roots))
print(unrealzeros, "<- leftover")

pnom_roots += pmath.stepwise_simplifier(pnom,pnom_roots,pmath.calc_multiplicities(pnom, pnom_roots))
print("All roots>>>", pnom_roots)

