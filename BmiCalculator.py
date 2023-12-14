def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    if not bmi or bmi <= 0:
        print("Invalid input. Please enter valid weight and height.")
    else:
        print(f"\nYour BMI is: {bmi:.2f}")
        category = classify_bmi(bmi)
        print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
