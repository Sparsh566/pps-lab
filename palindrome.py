# palindrome or not
def is_pal(s):
	s=s.lower()

	if s==s[::-1]:
		return "palindrome"
	else:
		return "not a palindrome"

string=input()
result=is_pal(string)

print(result)
