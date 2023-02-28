# BMI Calculator Advanced
ht = input("Enter your height in metres : ")
wt = input("Enter your weight in kgs : ")
bmi=(int(wt)/(float(ht)*float(ht)))
bmi=round(bmi,2)

if bmi<18.5 :
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi<=25:
    print(f"Your BMI is {bmi}, you have a normalweight")
elif bmi<=30 :
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi<=35 :
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")



