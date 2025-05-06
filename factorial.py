# factorial of given no
def factorial(n):
	if n<0:
		return "Enter a positive number"
	fact = 1
	for i in range(1,n+1):
		fact *= i
	return fact

def main():
	try:
		num = int(input("Enter a number : "))
		if num < 0:
			print("Enter a positive number")
		else:
			print(f"Factorial of given number is : {factorial(num)}")
	except ValueError:
		print("Enter a positive number")

if __name__ == "__main__":
	main()
