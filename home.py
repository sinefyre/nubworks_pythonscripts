#                                           home.py
#collection of scratch made code snippets, loosely secured, open-accessed and reusable modular fns
#                               Numerous and non-specific usecases
#                                           by: Sinefyre
#__________________________________________________________________________________________________#

#-----------------------------------------
#this function, given an integer, returns a list of its factors
#-----------------------------------------
def calc_factors(num):  #function that, given a number, returns a list of its factors
    li = []
    for arbx in range(num):
        #necessary to do a +1 shift so as to go with 1-15 inclusively as opposed to 0 to 14 <--- both counting styles have n-number indexes
        if(num%(arbx+1) == 0): #use of modulo to return remainder, 0 indicates full divisibility, thus a factor of n 
            li.append(arbx+1)
    return li

#-----------------------------------------
#this function, returns a bool value for if a given number is prime or not
#-----------------------------------------
def is_prime(num):  #function that, given a number, returns if it is infact prime or not
    factors = calc_factors(num)  #get factors of a given number
    if((len(factors) == 2) and (factors[0]==1 and factors[1]==num)):  #if it only has two factors, and they equal to 1 and itself, then it is prime
        return True
    else:
        return False

#-----------------------------------------
#this function, returns a bool value for if a given number is even or not
#-----------------------------------------
def is_even(num):   #function that, given a number, returns if it is infact even or not
    if(num%2 ==0): #if divisible by 2, it is even
        return True
    else:
        return False

#-----------------------------------------
#this function, returns a bool value for if a given number is odd or not
#-----------------------------------------
def is_odd(num):    #function that, given a number, returns if it is infact odd or not
    if(num%2>0): #will always be non-neg, but if 0 = is even, if >0 then it's not even but odd
        return True
    else:
        return False
        
#________________________________________________________________#
if __name__ == "__main__": 
    pass
   


   