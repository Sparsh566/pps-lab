# sum of digit of nos using recursion
def Sumof(n):
	if n==0:
		return 0
	else:
		return n%10+Sumof(n//10)

#Sumof

# take user input and add the function call
n=int(input())
result=Sumof(n)
print(result)
