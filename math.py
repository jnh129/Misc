'''
Author: Jonah Henry
This contains operations throughout logic, number theory, abstract algebra and set theory. 
I still have more classes to create and many more operations to add.
'''


import math

'''External functions are defined here'''
#{
def gcdCont(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcdCont(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcdCont(b, a % b)
#}        
''' End External Functions'''

class Logic():
    def __init__(self, b):
        if type(b) == bool:    
            self.b = b
        else:
            print("Error: Not of bool type")
            

    def and_(self, B):
        return self.b and B.b

    def or_(self, B):
        return self.b or B.b

    def onlyIf(self, B):
        if not self.b:
            result = True
        if self.b:
            if B.b == True:
                result = True
            else:
                result = False
        return result

    def ifThen(self, B):
        temp = Logic(B.b)
        return temp.onlyIf(self.b)
    
    def iff(self, B):
        return self.ifThen(B.b) and self.onlyIf(B.b)

##################################################
class MultiplicitiveGroup():
    
    def __init__(self, group, identity):
        self.set = group
        self.identity = identity
    def isGroup(self):
        for a in self.set:
            for b in self.set:
                if a*b not in self.set:
                    print("Not a group: closure error")
                    return False
        if self.set[0]*(self.set[1]*self.set[2]) != (self.set[0]*self.set[1])*self.set[2]:
            print("Not a group: associativity error")
            return False
        for a in self.set:
            if (self.identity*a != a) or (a*self.identity != a):
                print("Not a group: identity error")
                return False
        
                

##################################################
class Integer():

    def __init__(self, num = 1):
        self.n = num

    def isEven(self):
        return self.n % 2 == 0
    
    def isOdd(self):
        return not self.isEven()

    def isPrime(self):
        if self.n < 2:
            return False
        i = 2
        while i < self.n:
            m = Integer(i)
            if m.isPrime() == True:
                if self.n % i == 0:
                    return False
            i+=1
        return True

    def isPrimeOut(self, i = 0):
        print(i)
        if i != 0:
            n = 2
            while n < i:
                if i % n == 0:
                    return False
            return True
        else:
            pass

    def listPrimes(self):
        primes = []
        for i in range(2,self.n):
            if self.isPrimeOut(i) == True:
                primes.append(i)
        return primes

    def divides(self, m): #Returns self.n | m
        return m.n % self.n == 0

    def divisibility(self, m):
        return self.n % m == 0

    def getPrimeFactors(self):
        result = []
        i = 2
        while i <= self.n:
            if self.divisibility(i) == True:
                trial = Integer(i)
                if trial.isPrime == True:
                    result.append(i)
        return result

    def mod(self, a): #Finds self.n (mod a). That is, finds b s.t. a | (self.n - b)
        return self.n % a

    def __str__(self):
        return str(self.n)

    def getInt(self):
        return self.n

    def gcd(self, b):
        if b > self.n:
            if b % self.n == 0:
                return self.n
            else:
                return gcdCont(b % self.n, self.n)
        else:
            if self.n % b == 0:
                return b
            else:
                return gcdCont(b, self.n % b) 


##################################################

class Set():
    
    def __init__(self, inp = []):
        self.A = inp

    def size(self):
        return len(self.A)

    def cardinality(self):
        return self.A.size()

    def intersect(self, *B):
        intersect = []
        for elm in self.A:
            elm_remove = False
            for _set in B:
                if elm in _set:
                    if elm not in intersect:
                        if elm_remove == False:
                            intersect.append(elm)
                elif elm not in _set:
                    elm_remove = True
                    if elm in intersect:
                        intersect.remove(elm)             
        return intersect

    def union(self, *B):
        union = []
        for elm in self.A:
            if elm not in union:
                union.append(elm)
        for b in B:
            for belm in b:
                if belm not in union:
                    union.append(belm)
        return union

    def minus(self, B):
        minus = []
        for elem in self.A:
            if elem not in B:
                minus.append(elem)
        return minus

    def subtract(self, B):
        return self.minus(B)

    def remove(self, B):
        return self.minus(B)
    
##################################################

def main():
	pass


if __name__ == "__main__":
	main()