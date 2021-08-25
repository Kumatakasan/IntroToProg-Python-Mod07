# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# G.Kumataka, 8.20.2021, Started basic functions
# G.Kumataka, 8.23.2021, Finalized script and commented
# ------------------------------------------------- #
strStatus = ""

class Processor:

    #  This method checks if the input values were integers.
    @staticmethod
    def check_input_numbers(num1, num2):
        try:
            x = int(num1)
            y = int(num2)
            complex(x,y)
        except ValueError:
            return 'Fail'
        return 'Success'

    # This method does some math.  It returns a division error if the second number is 0.
    @staticmethod
    def do_some_math(num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        try:
            add = num1 + num2
            sub = abs(num1 - num2)
            div = num1 / num2
            mult = num1 * num2
            return add, sub, div, mult, "Success"
        except ZeroDivisionError:
            print("Second value input was zero!")
            print("Cannot divide by zero!")
            return None, None, None, None, "DivisionError"

class IO:

    # This method asks for user to input two values
    @staticmethod
    def number_input():
        print("Please enter two numbers between 0 and 50")
        num1 = input("First number is : ")
        num2 = input("Second number is : ")
        print()
        return num1, num2

# This code runs and calls the different functions to check.
int1, int2 = IO.number_input()
strStatus1 = Processor.check_input_numbers(int1, int2)

if strStatus1 == 'Success':
    add, sub, div, mult, strStatus2 = Processor.do_some_math(int1, int2)
    if strStatus2 == 'Success':
        print("The math was done and your values are: ")
        print("Addition= ", add, " Subtraction= ", sub, " Division= ", div, " Multiplication= ", mult)
    elif strStatus2 == 'Division_Error':
        print('The second input was zero and you cannot divide by zero!')
else:
    print("The values entered were not integers!")