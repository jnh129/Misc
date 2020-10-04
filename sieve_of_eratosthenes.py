''' Sieve of Eratosthenes: Returns primes less than or equal to a number'''

def is_prime(num):
	''' Checks if a number is prime'''
	if num <= 1:
		return False
	for i in range(2, int(num**(1/2))+1):
		if num % i == 0:
			return False
	return True

def sieve_of_eratosthenes(n):
	''' Returns primes less than or equal to a number '''
	nums = {}
	for i in range(2, n+1):
		nums[i] = True
	for key in nums:
		if nums[key] == False:
			pass
		else:
			if is_prime(key):
				j = 2
				while j*key <= n:
					nums[j*key] = False
					j+=1
			else: 
				pass
	return [key for key in nums if nums[key] == True]
