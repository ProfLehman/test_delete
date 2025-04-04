# Program: sprintconversion.py
# Name: Jan Busam
# Date: 2 April 2025
# Description: Convert sprint indoor times to outdoor times

# Input
name = input("Enter your name: ")

indoor = float(input("Enter your indoor time (in seconds): "))
    
# Processing
outdoor = indoor - 0.75

# Output
print(f"Athlete:", name)
print(f"Your indoor time is {indoor:.2f} seconds.")
print(f"Your estimated outdoor time is {outdoor:.2f} seconds.")