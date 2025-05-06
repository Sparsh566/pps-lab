#valid date
from datetime import date, timedelta

def is_val_da(year, month, day):
	try:
		return date(year, month, day)
	except ValueError:
		return None

def main():
	try:
		year = int(input("year: "))
		month = int(input("month: "))
		day = int(input("day: "))

		val_da = is_val_da(year, month, day)

		if val_da:
			print("valid")
			next_day = val_da + timedelta(days=1)
			print(f"incremented date: {next_day}")
		else:
			print("invalid")
	except ValueError:
		print("invalid")

if __name__=="__main__":
	main()
