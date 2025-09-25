height = int(input("Please enter your height (in):"))
weight = int(input("Please enter your weight (lbs):")) 

BMI = (int(weight) / (int(height)*int(height))) * 703

category = ("Underweight" if BMI < 18.5 else 
            "Normal" if 18.5 <= BMI < 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese")

reccomendation = ("maintain weight" if 18.5 <= BMI < 25 else
                  "gain weight" if BMI < 18.5 else
                  "lose weight" if 25 <= BMI < 30 else
                  "critical weight loss needed.")

healthrisk = ("low" if 18.5 <= BMI < 25 else
               "moderate" if BMI < 18.5 else
               "moderate" if 25 <= BMI < 30 else
               "high")

print(f" weight: {weight}, height: {height}, BMI: {BMI}, category: {category}, reccomendation: {reccomendation}, health risk: {healthrisk}")