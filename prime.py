def prime_numbers(num):
	factors=[]


	for i in range(2,num):
		if (num % i) !=0:
			print(num, "Prime!")
			break
		
			
		else:
			print(num,"is not a Prime number it's factors are:")
			#extend to ADD multiple values
			
			factors.extend([i,num//i,num])#number,number divided,and prime
			
			print(factors)
			break

#MAIN#
n = int(input("Enter a number: "))
if n>1:
	prime_numbers(n)
else:
	print("Invalid input Enter value bigger than 1")