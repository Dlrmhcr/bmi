height = float(input(" enter your height in meter: "))
weight = float(input("enter your weight in kg:"))
bmi = weight / (height) ** 2
if (bmi<18.15):
    print("you are underweight")
elif bmi<24.9:
    print("you are normalweight")
elif bmi<29.9:
    print ("you are overweight")
else:
    print ("you are obesity")

