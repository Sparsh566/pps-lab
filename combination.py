# combination of all digits 
from itertools import permutations

def is_val_di(digit):
	return 0 <= digit <= 9

def gen_com(d1,d2,d3):
	for perm in permutations([d1, d2, d3]):
		print("".join(map(str,perm)))

def main():
	try:
		d1 = int(input("digit1 (0-9): "))
		d2 = int(input("digit2 (0-9): "))
		d3 = int(input("digit3 (0-9): "))

		if is_val_di(d1) and is_val_di(d2) and is_val_di(d3):
			gen_com(d1, d2, d3)
		else:
			print("Invalid")
	except ValueError:
		print("Invalid")

if __name__=="__main__":
	main()
