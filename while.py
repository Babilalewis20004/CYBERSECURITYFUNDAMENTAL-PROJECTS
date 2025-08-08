# Initialize variables
total = 0
count = 0

# Start of while loop
while True:
    # Ask for input
    number = float(input("Enter a number: "))
    
    # Check if input is -1; if so, break out of loop
    if number == -1:
        break
    
    # Validate input; continue loop if 0 is entered
    elif number == 0:
        print("0 is not a valid input.")
        continue
    
    # Add valid inputs to total and increment count
    else:
        total += number
        count += 1

# Calculate average excluding -1 and 0; prevent division by zero error if no valid numbers were entered
average = total / count if count > 0 else None

# Print average or message indicating no valid inputs were received 
if average is not None:
    print(f"the mean is {average}")
else:
    print("No valid numbers were entered.")
