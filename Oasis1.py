def calculate_bmi(weight, height):

    return weight / (height ** 2)

def interpret_bmi(bmi):
    
    #Interpret BMI value and provide corresponding category.
    
    if bmi < 18.5:
        return "=> Underweight! <="
    elif bmi < 25:
        return "=> Normal weight <="
    elif bmi < 30:
        return "=> Overweight! <="
    else:
        return "=> Obese!! <="

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    print("Your BMI is: {:.2f}".format(bmi))
    
    category = interpret_bmi(bmi)
    print("You are considered:", category)

if __name__ == "__main__":
    main()
