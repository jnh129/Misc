
'''
Elementary prime and number functions
'''

def is_prime(p): #Primality test
    i = 2
    while i < p:
        if p % i == 0:
            return False
        else:
            i += 1
    return True

def is_prime_large(p): #Primality test for large numbers (faster)
    i = 2
    while i < p:
        if is_prime(i) == True:
            if p % i == 0:
                return False
            else: i += 1
        else:
            i += 1
    return True

def list_primes(n): #Lists primes less than n
    primes = []
    for i in range(2,n):
        if is_prime(i) == True:
            primes.append(i)
    return primes

def prime_divisors(p): #Creates a list of the prime factors of p
    div = []
    i = 2
    while i <= p:
        if is_prime(i) == True:
            if p % i == 0:
                div.append(i)
                i += 1
            else:
                i += 1
        else:
            i += 1
    return div

def prime_factorization(p): #Creates a dictionary of prime factors and their number of occurences
    fact = {}
    div = prime_divisors(p)
    for num in div:
        i = 1
        p1 = p/num
        while p1 % num == 0:
            i += 1
            p1 = p1/num
        fact[num] = i
        i = 1
        p1 = p
    return fact
        
def divides(a, b): #Checks if b|a
    if a % b == 0:
        return True
    else:
        return False
    
def largest_prime_divisor(n):
    p = n - 1
    while p > 2:
        if divides(n, p) == True:
            if is_prime(p) == True:
                return(p)
            else:
                p = p - 1
        else:
            p = p - 1

def common_divisors(m, n):
    div = []
    j = 1
    while j <= m and j <= n:
        if m % j == 0 and n % j == 0:
            div.append(j)
            j += 1
        else:
            j += 1
    return div

def gcd(m, n):
    divisors = common_divisors(m, n)
    return divisors[-1]

def relatively_prime(m, n):
    if gcd(m, n) == 1:
        return True
    else:
        return False
    
def is_even(n): #True = even, False = odd
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_odd(n): #True = odd, False = even
    if n % 2 != 0:
        return True
    else:
        return False

def twin_primes(n): #Returns all pairs of twin primes not exceding n 
    pairs = []
    p1 = 2
    while p1 <= (n-2):
        occurance = []
        p2 = p1 + 2
        if is_prime(p1) == True:
            occurance.append(p1)
            occurance.append(p2)
            if is_prime(p2) == True:
                pairs.append(occurance)
                p1 += 1
            else:
                p1 += 1
        else:
            p1 += 1
    return pairs

def relative_prime(a,b): #True = relatively prime, #False = not relatively prime
    if a == 1 or b == 1:
        return True
    elif a == b:
        return False
    else:
        c = 2
        while c < a:
            if a % c == 0:
                if b % c == 0:
                    return False
                else:
                    c += 1
            else:
                c += 1
        return True

def pi(n):
    i = 0
    p = 2
    while p <= n:
        if is_prime(p) == True:
            i += 1
            p += 1
        else:
            p += 1
    return i

def pi_large(n): #Approximates pi(n) for large integers
    import math
    m = n/(math.log(n,[math.e]))
    return m

def Goldbach_Conjecture(n):
    if is_even(n) == False:
        return(n, "is odd")
    elif is_even(n) == True:
        primes = list_primes(n)
        for p1 in primes:
            for p2 in primes:
                m = p1 + p2
                if m == n:
                    return p1, p2
                
 
'''
Elementary congruence functions
'''

def congruence(a,m):
    for b in range(m):
        p = abs(a-b)
        if p % m == 0:
            return b


def congruence_test(a, b, m): #Checks if a (mod m) = b
    p = abs(a-b)
    if p % m == 0:
        return True
    else:
        return False

def modular_inverse(a, m): #Finds the modular inverse of a (mod m), if one exists
    i = 1
    while i < m:
            b = a*i - 1
            if b % m == 0:
                return i
            else:
                i += 1
    return False

def mod_inverse_test(a, b, m): #Tests if b is the inverse of a (mod m)
    n = a * b - 1
    if n % m == 0:
        return True
    else:
        return False

def all_modular_inverse(m): #Finds all the modular inverses modulo m
    d = {}
    for a in range(m):
        inv = modular_inverse(a, m)
        if inv != False:
            d[a] = inv
    return d

def quadratic_residue_test(a,m):
    if relative_prime(a, m) == True:
        x = 1
        while x < m:
            y = x**2
            if y % a == m:
                return True
            else:
                x += 1
        return False
    else:
        return False

def quadratic_residues(m):
    d = []
    for a in range(1, m):
        if quadratic_residue_test(a,m) == True:
            d.append(a)
    return d

'''
Other stuff for now
'''

def f(x):
    pass

def fun(xmin, xmax):
    d = {}
    for i in range(xmin, xmax + 1):
        d[i] = f(i)
    return d

'''
Collatz Conjecture
'''

def Collatz(n):
    i = 0
    if n == 1:
        return i
    else:
        while n != 1:
            if n % 2 == 0:
                n = n/2
                i += 1
            elif n % 2 == 1:
                n = 3*n+1
                i += 1
    return i

def do_Collatz(i):
    d = {}
    for n in range(1, i + 1):
        coln = Collatz(n)
        d[n] = coln
    return d

def do_Collatz_Primes(i):
    d = {}
    p = 2
    while p <= i:
        if is_prime(p) == True:
            d[p] = Collatz(p)
            p += 1
        elif is_prime(p) == False:
            p += 1
    return d

def Collatz_main():
    trials = int(input("Enter a positive integer: "))
    col_dict = do_Collatz(trials)
    print(col_dict)

'''
Recursion
'''

def Fibonacci():
    fib = [1, 1]
    f0 = 1
    f1 = 1
    iterations = int(input("Choose the number of iterations: "))
    for i in range(0, iterations - 2):
        fk1 = f0 + f1
        fib.append(fk1)
        f0 = f1
        f1 = fk1
    return fib

def sumn(n):
    return int(n*(n+1)/2)

'''
Multiplicitive Functions
'''

def Euler_Phi(n):
    pfact = prime_factorization(n)
    plist = list(pfact.keys())
    Phi = 1
    for prime in plist:
        Phi = Phi*((prime**pfact[prime])-(prime**(pfact[prime]-1)))
    return Phi

def sum_divisors(n):
    div_sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            div_sum += i
    return div_sum

def num_of_divisors(n):
    num = 0
    for i in range(1, n+1):
        if n % i == 0:
            num += 1
    return num      

def is_perfect(n): #Tests if n is a perfect number
    m = Sum_Divisors(n)
    if m == 2*n:
        return True
    else:
        return False

'''
Legendre Symbol
'''

def Legendre_Symbol(a, m):
    if quadratic_residue_test(a,m) == True:
        return(1)
    else:
        return(-1)

'''
Create the main function here
'''

def main():
    pass

if __name__ == "__main__":
	main()



