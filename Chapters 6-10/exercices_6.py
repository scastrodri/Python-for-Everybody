# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards 
# to the first character in the string, printing each letter on a separate line, except backwards.

index = 0
fruit = 'banana'

while index < len(fruit):
    try:
        letter = fruit[index-1]
    except:
        exit()
    print(letter)
    index = index - 1

# Exercise 4: There is a string method called count that is similar to the function in the previous exercise. 
# Read the documentation of this https://docs.python.org/library/stdtypes.html#string-methods Write an invocation 
# that counts the number of times the letter a occurs in “banana”

word = 'banana'
print(word.count('a'))

# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475' Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'
print(float(str[str.find(':')+1:]))