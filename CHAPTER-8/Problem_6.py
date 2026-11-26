# Write a python function which converts inches to cms

def inch_to_cms(inch):
    return inch * 2.54

inch = int(input("Enter a value in inch:"))

print(f"The corresponding value in cms is {inch_to_cms(inch)}")