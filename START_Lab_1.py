def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb*1073741824 # 1 gigabytes is equivalent to 1073741824 bytes

    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    string_count = 0

    if (type(name) == str) & (len(name) > 0):
        string_count = len(name) % 2
        if string_count == 1:
            is_odd = True
        else:
            is_odd = False
    else:
        is_odd = None

    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if input_number <= len(input_string)-1:
        character_at = input_string[input_number]
    else:
        character_at = -1

    return character_at

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    
    with open(file_name, 'r') as file:
        file_string = file.readlines()
        list_of_nums = [eval(i) for i in file_string]

    return list_of_nums

def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    single_mode_value = 1

    def mode_grabber(input):
        unique_numbers = []
        mode_numbers = []

        for i in input:
            if i not in unique_numbers:
                unique_numbers.append(i)
            else:
                mode_numbers.append(i)
        
        return mode_numbers
    
    value_checker = mode_grabber(list_numbers)
    while single_mode_value < len(value_checker):
        value_checker = mode_grabber(value_checker)

    mode_of_list = value_checker[0]
    
    return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    
    total = round((quarters/4) + (dimes/10) + (nickels/20) + (pennies/100),2)

    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.