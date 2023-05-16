weight = input("weight: ")
unit=input("(L)bs or (K)g: ")
if unit.upper()=="K":
	conversion=int(weight)//0.45
	print(f"You weigh {conversion}pounds")
else:
	conversion=int(weight)*0.45
	print(f"You weigh {conversion}kilograms")