# sum of digits of no
def sum_digit(num):
	total=0
	while num>0:
		total += num%10
		num = num//10
	return total

num=int(input("num: "))
print(f"sum: {sum_digit(num)}")
