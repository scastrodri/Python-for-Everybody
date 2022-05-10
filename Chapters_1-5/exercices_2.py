# I'm not going to consider mistakes in the inputs yet

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
print('Enter your name: ', )
name = input('')
print ('Hello ',name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
print ('Pay: ', hours * rate)

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to 
# Fahrenheit, and print out the converted temperature.
celsius = float(input('Enter Celsius temperature: '))
print ('The Fahrenheit temperature is: ', celsius * 9/5 + 32)