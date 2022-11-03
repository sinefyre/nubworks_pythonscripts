#                                           pmath Module
#Custom module containing functions related to synthetic division and polynomial root finding
#                                           by: Sinefyre
#__________________________________________________________________________________________________#


#-----------------------------------------
# this function, given a string converts (to an int) an numeric-string into an actual integer equivalent
#-----------------------------------------
def int_conv(str_item): 
    return int(str_item)   #ex "10"  --> 10

#-----------------------------------------
#this function applies int_con() to a whole string, makes a list of numbers deliniated f/ string w/ commas
#-----------------------------------------
def process_pnom(string): 
    return list(map(int_conv, string.split(",")))  #done via map, split, and result collection converted to list type

#-----------------------------------------
#this function, given two lists, returns the quotient of them, aka p/q values, possible real rational roots
#-----------------------------------------
def calc_possible_zeros(p_factors,q_factors):
    #using list to set to list conversion to remove dupes
    p_by_q = [] #This set follows a 2D array whereby every p,pairs with a q divisor basically
    
    for arbx in range(len(p_factors)):  #using a nested for loop to iterate the way we need to for p/q collection
        for arby in range(len(q_factors)):
            p_by_q.append(p_factors[arbx]/q_factors[arby])
    
    #list comp to make list w/ removed dupes via python [*set(collectionType)]  feature
    return [*set(p_by_q)] #elsewhere, these values will be evaluated on a pos, neg basis

#-----------------------------------------
#this function, given some number, tells if above or below zero
#-----------------------------------------
def sign_state(num):
    if(num <0):
        return "negative"
    else:
        return "positive"

#-----------------------------------------
#this function, given a list, polynom,  outputs sign change amount
#-----------------------------------------
def descartian_calc(polynom):
    polynom = clear_val(polynom,0) #given the list of numbers, polynom, it returns a new one with all 0's in it removed
    sign_count = 0 #variable will hold, number of instances a sign change occurs in the aforementioned list
    for x in range(len(polynom)-1): #0th to cardinalityOfGroupEntity-1 iter
        local_state_A= sign_state(polynom[x])
        local_state_B= sign_state(polynom[x+1])
        if(local_state_A != local_state_B): #per iter compares 'local state'current index val and its next, if not equal it counts as sign change
            sign_count+=1   #whole for loop ceases at len(Polynom)-1 but does not go out of index because at that points, contents not inclusive
    #note: Can add additional(lol) directly counting code to capture exact sign change or neg and pos should their be some issue 11/02/2022
    return sign_count

#-----------------------------------------
#this function, given an iterable collection,ex: list of ints, returns one with numeric-zero's removed
#-----------------------------------------
def clear_val(collection,num): # if num said to be, say, zero, then below it will return a list with all except value of zero
    new_coll = []
    for x in range(len(collection)): 
        if(collection[x] != num):
            new_coll.append(collection[x])
    return new_coll #size is either less than original, if zeros excised, or the same if no zeros in original

#-----------------------------------------
#this function, given a list of polynomial coefficients, will return a list of all (actual) real reational roots 
#-----------------------------------------
def calc_pnom_roots(polynom):
    p_value = polynom[len(polynom)-1]  #ex: y = 1x^3+6x^2+10x-9   the constant is the last, value as -9, which we get by len#-1 indexwise
    q_value = polynom[0] #for the example above, this would be lead coeficient or order wise, the first  value as +1
    
    import home #Need to get fn that generates a list of factors given an integer as input
    #two if statements below are for if p or q is negative, we want it positive for simple implement (Neg root possibility handled downstream)
    if(p_value<0):
        p_value=p_value*-1
    if(q_value<0):
        q_value=q_value*-1
    #two lines below give us our factors of p and q
    p_facts = home.calc_factors(p_value)
    q_facts = home.calc_factors(q_value)

    c_val = calc_possible_zeros(p_facts, q_facts) #gets a list of possible, but not necessarily actual real rational roots
    c_val = c_val + [-1*x for x in c_val]  #use of list comp to add on a list of additive inverses (aka our negative rational roots)
    c_val = process_rats(polynom, c_val) #gets list of actual real rational roots
    return sorted(c_val)  #return real rational roots, sorted in ascending order

#-----------------------------------------
#this function, simply given a list,polynom, and an int, root_val, uses the int as a root on polynom and DOES synthetic division
#-----------------------------------------
def calc_pnom_quotient(polynom, root_val):
    quotient_pnom = []
    for x in range(len(polynom)):
        if(x==0):
            quotient_pnom.insert(0, polynom[0])#init dropdown of first value in syndiv algo
        if(x>0 and x<=len(polynom)-1): #for all beyond the 0th index
            quotient_pnom.append(polynom[x]+(quotient_pnom[x-1]*root_val))
    return quotient_pnom  #Interp: if last index 0, that's the remainder, means that the used root is in fact a real root aka zero of said polynom

#-----------------------------------------
#this function, given a list, polynom, and a list, roots will evaluate actual real rat roots of the polynomial given
#-----------------------------------------
def process_rats(polynom, roots):
    true_real_rats = [] #list for actual real rational roots
    #for loop to iterate through each root
    for x in range(len(roots)):
        temp_list = calc_pnom_quotient(polynom,roots[x]) #temporary list made to hold contrasts and filter for actuals
        if(temp_list[len(temp_list)-1] == 0.0): #per iteration, IF this lists last index, aka remainder slot, IS a zero. . .
            true_real_rats.append(roots[x])  #THEN it will be appended to the list for actual, real rat roots

    del temp_list #data management practice, might as well delete expended entities after their usecase
    return true_real_rats #returns out list of actual real rat roots
        
#-----------------------------------------
#this function, given two lists, one the polynom, and its actual roots, will return a list of multiplicities 
#of every element in matched order to roots(aka 2nd) list  --->As 11/02/2022 may need to amend, a root multiplicity may exceed total # of unique root counts
#-----------------------------------------
def calc_multiplicities(polynom, roots):
    multiplicity_set=[]
    for n in range(len(roots)):  #external for-loop to make iters over all roots
        mult_ct = 0 #resets to zero per whole iter
        
        temp_list = calc_pnom_quotient(polynom, roots[n]) #syndiv polynom via root element per iter
        count=n #Will be fixed, post 11/02/2022
        
        while(count<len(roots)): #internal most loop, pivotal for, per a root, seeing how many times it yields as a zero of polynom list
            if(temp_list[len(temp_list)-1]==0):
                mult_ct+=1
            temp_list= calc_pnom_quotient(temp_list,roots[n])
            count+=1 #count here serves to help us iter through and then end out the internal loop 
        multiplicity_set.append(mult_ct)#and we end per iter over root ele with an append of a multiplicity of respective nth index root
    return multiplicity_set

#-----------------------------------------
#this function, factors in stepwise fashion, a polynomial using its action real rat roots,
#and after reaching a degree of 2, solves a quadratic and will yield actual unreal roots
#-----------------------------------------
def stepwise_simplifier(polynom,roots,mult_set):
    for x in range(len(roots)):
        n=0
        while(n<mult_set[x]):
            temp_pn = calc_pnom_quotient(polynom, roots[x])
            del temp_pn[len(temp_pn)-1]
            #print(temp_pn, "resultant temp pnom", roots[x], "<= associated root")
            n+=1
            polynom = temp_pn
    if(len(temp_pn)==3): #Because only when an polynomial can't be solved, and we are stuck at degree=2, we get a quadratic that yields unreal nums
        temp_pn = list(get_unreal_roots(temp_pn)) #gets unreal roots
        return temp_pn
    else: #if not the case, that is, if no unreals it will not return anything. SO TO ABOVE COMMENT might not have to go
        return "" 

#-----------------------------------------
#this function, simply gets unreal roots, aka it's  just solving a quadratic eqn
#-----------------------------------------
def get_unreal_roots(polynom):
    from qmath import qfrm
    return qfrm(polynom[0],polynom[1],polynom[2])


