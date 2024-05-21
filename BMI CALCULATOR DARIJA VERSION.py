def calculate_BMI(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("Mer7ba bik in the BMI CALCULATOR")

    # Get user input
    weight = float(input("De5el ch7al fik men kilo: "))
    height = float(input("De5el tol dyalek ex: 1.75: "))

    # Calculate BMI
    bmi = calculate_BMI(weight, height)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")

    # Interpret the result
    if bmi < 18.5:
        print("SIR a5oya GOL LIK CHWIYA RAK atmout b jou3. *Underweight*.")
    elif 18.5 <= bmi < 24.9:
        print("MA3LIKCH RAK MAZYAN. *Normal weight*.")
    elif 25 <= bmi < 29.9:
        print("5OYA wla 5ti sir n9ess lmakla o dir lik chwiya dyal sport rah lbola L7AMRA 9erbat tech3el *overweight*.")
    else:
        print("5OYA WLA 5ti lbola lamra cha3lat rak 8lid n9ess lmakla chwiya o dir bazzaaaf dyal sport *You_90are_obese*.")

# Run the main function
if __name__ == "__main__":
    main()


