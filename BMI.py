# calculates bmi from weight and height
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# tells what the bmi number means
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese weight"

# main part of the program
def main():
    try:
        # get weight and height from user
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        # calculate and explain BMI
        bmi = calculate_bmi(weight, height)
        result = interpret_bmi(bmi)

        # show the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {result}")

    except ValueError:
        # if user enters wrong input
        print("Please enter a valid number.")

# runs the main function when file is opened directly
if __name__ == "__main__":
    main()