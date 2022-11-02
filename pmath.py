#functions related to some polynomial stuffs, stuff not necessarily in numpy to my knowledge


# this function simply converts an numeric-string into a visual integer equivalent
def int_conv(str_item): 
    return int(str_item)   #ex "10"  --> 10


#this function simply converts a whole string of text-numerics to integer numerics, delinating by comma
def process_pnom(string): 
    return list(map(int_conv, string.split(",")))  #map(),split() used to systematically delineate a number from the next


#this function, given two lists, returns the quotient of them, aka p/q values, possible ratn real zeros
def process_testzeros(p_factors,q_factors):
    #using list to set to list conversion to remove dupes
    p_by_q = [] #This set follows a 2D array whereby every p,pairs with a q divisor basically
    
    for arbx in range(len(p_factors)):  #using a nested for loop to iterate the way we need to for p/q collection
        for arby in range(len(q_factors)):
            p_by_q.append(p_factors[arbx]/q_factors[arby])
    
    #now we need to remove dupes via  pythonic [*set()]  feature, see useful links below
    return [*set(p_by_q)] #elsewhere, these values will be evaluated on a pos, neg basis

#this function, given some number, tells if above or below zero
def sign_state(num):
    if(num <0):
        return "negative"
    else:
        return "positive"

#this function, given a pnom outputs anticipated pos, neg
def descartian_calc(polynom):
    polynom = clear_val(polynom,0) #given the list it returns a new one with all numeric-zero rmv'd
    sign_count = 0
    for x in range(len(polynom)-1):
        local_state_A= sign_state(polynom[x])
        local_state_B= sign_state(polynom[x+1])
        if(local_state_A != local_state_B):
            sign_count+=1 
    return sign_count

#this function, given an iterable, particularly like a list of integers, returns one with numeric-zero removed
def clear_val(collection,num):
    new_coll = []
    for x in range(len(collection)): 
        if(collection[x] != num):
            new_coll.append(collection[x])
    return new_coll


#this function, also called calc_unprocessed_roots, is the pmath version, not home. 
def calc_pnom_roots(polynom):
    p_value = polynom[len(polynom)-1]  #ex: y = 1x^3+6x^2+10x-9   the constant is the last, value as -9, which we get by len#-1 indexwise
    q_value = polynom[0] #for the example above, this would be lead coeficient or order wise, the first  hence 1
    #in a nutshell p is the last value of our list, q is the first value of the list, placewise
    #print("end-term = {}\nlead-term = {}".format(p_value,q_value))
    import home
    if(p_value<0):
        p_value=p_value*-1
    if(q_value<0):
        q_value=q_value*-1
    p_facts = home.calc_factors(p_value)
    q_facts = home.calc_factors(q_value)

    #print(p_factors, "<-factors of p\n", q_factors, "<-factors of q")
    c_val = process_testzeros(p_facts, q_facts)
    c_val = c_val + [-1*x for x in c_val]  #processes possible zeros
    c_val = process_rats(polynom, c_val)
    return sorted(c_val)

#this function, given the polynomial and it's calculated possible rational roots, will return the resultant quotient from syndiv
def calc_pnom_quotient(polynom, root_val):
    quotient_pnom = []
    for x in range(len(polynom)):
        if(x==0):
            quotient_pnom.insert(0, polynom[0])
        if(x>0 and x<=len(polynom)-1): #for all beyond the 0th index
            quotient_pnom.append(polynom[x]+(quotient_pnom[x-1]*root_val))
        #if last index 0, that's the remainder, means that the used root is in fact a real root aka zero of said polynom
    return quotient_pnom  

def process_rats(polynom, roots):
    true_real_rats = [] #actual real rational roots
    for x in range(len(roots)):
        temp_list = calc_pnom_quotient(polynom,roots[x])
        if(temp_list[len(temp_list)-1] == 0.0):
            true_real_rats.append(roots[x])
    del temp_list
    return true_real_rats
        
def calc_multiplicities(polynom, roots):
    multiplicity_set=[]
    for n in range(len(roots)):
        mult_ct = 0
        
        temp_list = calc_pnom_quotient(polynom, roots[n])
        count=n
        
        while(count<len(roots)):
            if(temp_list[len(temp_list)-1]==0):
                mult_ct+=1
            temp_list= calc_pnom_quotient(temp_list,roots[n])
            count+=1
        multiplicity_set.append(mult_ct)
        
    return multiplicity_set

#used to stepwise factor a polynomials real roots (rational reals) to get the part w/  unreal roots
def stepwise_simplifier(polynom,roots,mult_set):
    for x in range(len(roots)):
        n=0
        while(n<mult_set[x]):
            temp_pn = calc_pnom_quotient(polynom, roots[x])
            del temp_pn[len(temp_pn)-1]
            #print(temp_pn, "resultant temp pnom", roots[x], "<= associated root")
            n+=1
            polynom = temp_pn
    if(len(temp_pn)==3):
        temp_pn = list(get_unreal_roots(temp_pn))
        return temp_pn
    else:
        return ""

def get_unreal_roots(polynom):
    from qmath import qfrm
    return qfrm(polynom[0],polynom[1],polynom[2])


#def calc_final_quotient (quotient):
#    final_breakdown = []