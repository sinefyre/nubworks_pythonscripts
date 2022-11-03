#                                           csynth.py
#script utilizing functions from custom module pmath, to solve for roots(real rational, and unreal roots) of a polynomial
#                                           by: Sinefyre
#__________________________________________________________________________________________________#

#User enter's a group of integers seperated by a comma
pnom = input("Enter orderly coefs sep'd by comma\nExample>>1,2,3,4....\n>>") #currently is a string

import pmath 

pnom = pmath.process_pnom(pnom)   #converts the string into a list of integers

pnom_roots= pmath.calc_pnom_roots(pnom) #generates the actual real rational roots given the list aka polynomial above, sorted low to high value
print(pnom_roots , "<-polynomial roots set\n\n")

pnom_multiplicites_set = pmath.calc_multiplicities(pnom, pnom_roots)#we get respective multiplicites in order to aforementioned list in ascending order
print(pnom_multiplicites_set, "<- are ordered multiplicities")

unrealzeros = pmath.stepwise_simplifier(pnom,pnom_roots,pnom_multiplicites_set) #calculate list of unreal roots 
print(unrealzeros, "<- leftover")

pnom_roots += pmath.stepwise_simplifier(pnom,pnom_roots,pnom_multiplicites_set) #combiing actual real rats w/ unreal roots
print("All rat roots;Real and unreals>>>", pnom_roots)

