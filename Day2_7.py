# BMI Calculator
ht = input("Enter your height in metres : ")
wt = input("Enter your weight in kgs : ")
bmi=(int(wt)/(float(ht)*float(ht)))
print("BMI : "+str(bmi))
print(f"BMI : {bmi}")