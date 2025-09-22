height = int(input("Please enter your height (in):"))
weight = int(input("Please enter your weight (lbs):"))

BMI = (int(weight) / int(height^2)) * 703

category = ("Underweight" if BMI < 18.5 else 
            "Normal" if 18.5 <= BMI < 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese")

print(f" weight: {weight}, height: {height}, BMI: {BMI}, category: {category}")