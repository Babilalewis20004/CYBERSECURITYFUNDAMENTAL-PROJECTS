# getting users data
str_manip = input("enter a sentence: ")
#displaying and working out the length
length = len(str_manip)
print(length)
# getting the last character from the string
last_letter = str_manip[-1:]
print(last_letter)
swap_string = str_manip.replace(last_letter, '@') 
print(swap_string)
#displaying the last 3 characters backward
backward_str = swap_string [-3:][::-1]
print(backward_str)
# joing the first 3 and last 2 characters
five_letter = str_manip[:3] + str_manip[-2:]
print(five_letter)
   
    
