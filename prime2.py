def print_primerange(new_min,new_max): 

	print("Prime numbers in the range:",new_min,new_max)
	primes=[]
	for num in range(new_min,new_max):
		if num > 1:
			for i in range(2,num):
				#for specidied range check num
				if (num % i) == 0:
					break
			else:
				primes.append(num)
				print(primes)

#main#
print("Specify a range of numbers")
min= int(input("Define minimum number:"))
max = int(input("Define maximum number:"))
print_primerange(min,max)