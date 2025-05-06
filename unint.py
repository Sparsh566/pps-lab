#union,intersection and difference
a= list(map(int,input("set a: ").split()))
A=set(a)
b= list(map(int,input("set b: ").split()))
B=set(b)

un_set = A|B
inte_set = A&B
diff_set = A-B

print(f"Union: {un_set}")
print(f"Intersection: {inte_set}")
print(f"Difference: {diff_set}")
