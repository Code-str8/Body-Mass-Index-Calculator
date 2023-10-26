def calculate_bmi(height, weight):
     # calculate bmi = weight / height^2
    return weight / (height ** 2)

print("Please enter your height in meters and weight in kilograms.")

try:
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
bmi = calculate_bmi(height, weight)
print(f"Your BMI is: {bmi:.2f}")