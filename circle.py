#circle
rad = float(input("Enter the radius: "))

if rad<0 or rad>100:
    print("Enter a positive value upto 100")
else:
    pi=3.18
    area=pi*rad*rad
    print(f"Area of circle = {area:.6f}")
