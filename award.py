swim = int(input("Enter swim time in minutes: "))
cycle = int(input("Enter cycle time in minutes: "))
run = int(input("Enter run time in minutes: "))
    
total_time = swim + cycle + run
print("the total time is: ", total_time)



if total_time <= 100:
        print("Honorary colours")
elif 101 <= total_time <= 105:
        print("Honorary half colours")
elif 106 <= total_time <= 110:
        print("Honorary scroll")
else:
         print("No award")


    
    


