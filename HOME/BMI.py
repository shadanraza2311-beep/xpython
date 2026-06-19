print(60*"#")
print(22*"#" ,"BMI CALCULATOR", 22*"#")
Height_cm = int(input("Enter your Height : "))
Weight_kg = int(input("Enter your weight : "))
BMI = (Weight_kg*10000)/(Height_cm*Height_cm)
print( "your BMI is ==>" ,BMI)
print(60*"#")
if BMI < 18:
	print(10*"=" ,"Underweight")
elif BMI < 25 :
	print(10*"=" ,"NORMAL")
elif BMI < 30:
	print(10*"=", "OVERWEIGHT")
else:
	print("Invalid")