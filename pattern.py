#pattern
def print_pattt(n):
	for i in range(n, 0, -1):
		print('* '*i)

def main():
	try:
		num = int(input("Enter a number : "))
		if num<0:
			print("Enter a positive number")
		else:
			print_pattt(num)
	except ValueError:
		print("Enter a positve number")

if __name__=="__main__":
	main()
