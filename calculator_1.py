#the first calculator for 2 number


# import calculator_function as calc
from os import system
from calculator_function import add, sub, mult, div


def main():
    """Main python calculator application"""
    system('cls')
    print('Welcome to Paraclete\'s Calculator')

    while True:

        print(""" \n\n
              press 1: To add 2 numbers
              press 2: To substract 2 numbers
              press 3: To divide 2 numbers
              press 4: To multiply 2 numbers
              press 5: To Exit
              
              \n\n""")

        option = input('input options between 1 - 5: ')

        if option == '5':
            print('\nExiting .....')
            break
        if option not in ['1', '2', '3', '4', '5']:
            print('Invalid option select between option (1-5)')
            continue

        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if option == ('1'):
            print(f"Result: {add(num1, num2)}")
        elif option == ('2'):
            print(f"Result: {sub(num1, num2)}")
        elif option == ('3'):
            print(f"Result: {div(num1, num2)}")
        elif option == ('4'):
            print(f"Result: {mult(num1, num2)}")
        else:
            print("invalid option")



if __name__ == "__main__":
    main()