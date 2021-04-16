# Austin Rowell, arr461
# QA Assignment 2
# Due: Thursday, March 4th 2021
# Program for calculating BMI and Retirement

# Imports
import argparse
from consolemenu import *
from consolemenu.items import *
from getch import getch, pause
from flask import Flask

# Fucntion to populate Menu    
def menu():
    
    menu = ConsoleMenu("QA Assignment 2", "Assignment done in Python 3.9.2")
    command_retire = CommandItem("Retirement Calculation",  ".\QA_Assignment.py -r")
    menu.append_item(command_retire)
    command_BMI = CommandItem("BodyMassIndex Calculation",  ".\QA_Assignment.py -b")
    menu.append_item(command_BMI)
    
    primary = menu

    # Pass primary for every function to show menu
    return primary
    
# Calculate Retirement
def retirement(primary):

    # Inputs from user
    c_age = int(input("Please enter your current age: "))
    a_salary = int(input("Please enter your annual salary: "))
    s_goal = int(input("Please enter your savings goal: "))
    p_saved = int(input("Please enter your percentage saved: ")) * 0.01

    # Calculate Answer
    s_per_year = (a_salary * p_saved ) * 1.35
    years_goal = s_goal / s_per_year
    age_met = c_age + years_goal
    age_met = round(age_met)

    # Confirm age is below target
    if age_met < 100:
        print("Savings age goal will be: {}\n".format(age_met))
    else:
        print("Saving age exceeds 100 years of age...\n")
        
    
    primary.show()

    return(age_met)

# Calculate BMI 
def BMI(primary):

    # User input and Calculate BMI
    feet_inches = input("How many feet and inches are you? (Seperate by a space)").split()
    total_inches = int(feet_inches[0]) * 12 + int(feet_inches[1])
    meters = (total_inches * 0.025) * (total_inches * 0.025)
    kilograms = float(input("How much do you weigh?")) * 0.45
    actual_BMI = round(kilograms/meters)

    # Correctly state classification of BMI
    if actual_BMI <= 18.5:
        print("You are classified as: Underweight ({})\n".format(actual_BMI))
    elif actual_BMI > 18.5 and actual_BMI < 24.9:
        print("You are classified as: Normal Weight ({})\n".format(actual_BMI))
    elif actual_BMI > 25 and actual_BMI < 29.9:
        print("You are classified as: Overweight ({})\n".format(actual_BMI))
    elif actual_BMI > 30:
        print("You are classified as: Obese ({})\n".format(actual_BMI))

    
    primary.show()

    return (actual_BMI)

# Parser function for command line    
def parser(primary):

    parser = argparse.ArgumentParser()

    # Add two arguments ( -b -> BodyMassIndex, -r -> Retirement ) for command line
    parser.add_argument("-b", "--BodyMassIndex", help="Solve Body Mass Index",
                    action="store_true")
    parser.add_argument("-r", "--Retirement", help="Solve Retirement",
                    action="store_true")

    args = parser.parse_args()

    parser.parse_args()

    # Determines which argument is true 
    if args.Retirement:
        retirement(primary)

    if args.BodyMassIndex:
        BMI(primary)

# Main Function        
def main():

    # Create Menu
    primary = menu()

    # Parse command argument
    parser(primary)

main()
