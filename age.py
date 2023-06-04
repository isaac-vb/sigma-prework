from datetime import datetime
import math

def calculate_age(date_str):
    current_date = datetime.now().date()
    date_of_birth = datetime.strptime(date_str, "%d/%m/%Y").date()
    difference = current_date - date_of_birth
    return difference.days

# Example usage
date_of_birth_str = input("Enter a date (DD/MM/YYYY): ")
age= calculate_age(date_of_birth_str) #age in days

decimal_years =(age/365) - int(age/365)
print("You are ",math.floor(age/365.25) ," years old")
if(decimal_years>0.8):
    print("But you are almost ", math.ceil(age/365.25), "!")
