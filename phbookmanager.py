#phone book manager
def add_con(ph_bk):
	name=input("Name: ")
	ph_no=input("Phone number: ")
	ph_bk[name]=ph_no

def rem_con(ph_bk):
	name=input("Name: ")
	if name in ph_bk:
		del ph_bk[name]
	else:
		print("Not found")

def dis_con(ph_bk):
	if ph_bk:
		print(ph_bk)
	else:
		print("{}")

ph_bk = {}

while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")

	choice = input("Enter choice (1-4): ")

	if choice == '1':
		add_con(ph_bk)
	elif choice == '2':
		rem_con(ph_bk)
	elif choice == '3':
		dis_con(ph_bk)
	elif choice == '4':
		break
	else:
		print("Invalid")
