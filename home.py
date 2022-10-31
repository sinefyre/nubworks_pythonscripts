2#collection of scratch made code snippets, loosely secured, open-accessed and reusable modular fns or vars (aka module) aka just'a py script bro


def calc_factors(num):  #function that, given a number, returns a list of its factors
    li = []
    for arbx in range(num):
        #necessary to do a +1 shift so as to go with 1-15 inclusively as opposed to 0 to 14 <--- both counting styles have n-number indecies
        if(num%(arbx+1) == 0): #use of modulo to return remainder, 0 indicates full divisibility, thus a factor of n 
            li.append(arbx+1)
    return li


def is_prime(num):  #function that, given a number, returns if it is infact prime or not
    factors = calc_factors(num)  #get factors of a given number
    if((len(factors) == 2) and (factors[0]==1 and factors[1]==num)):  #if it only has two factors, and they equal to 1 and itself, then it is prime
        return True
    else:
        return False


def is_even(num):   #function that, given a number, returns if it is infact even or not
    if(num%2 ==0): 
        return True
    else:
        return False

def is_odd(num):    #function that, given a number, returns if it is infact odd or not
    if(num%2>0):
        if(num%3==0):
            return True
    else:
        return False
        
if __name__ == "__main__": 
    
    pass
   
   
   
   #extra resources
   #https://www.livescience.com/34526-prime-numbers.html#:~:text=A%20prime%20number%20is%20an,except%20for%201%20and%203. primes are only integers
   #https://www.mathsisfun.com/numbers/even-odd.html  even and odd refer to categories of integer numbers 
   