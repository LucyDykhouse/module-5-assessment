# Opens the file 'um-server-01.txt' and returns it as a file object
log_file = open("um-server-01.txt")

# Defines a function 'sales_reports' that takes in the variable 'log_file'
def sales_reports(log_file):
    for line in log_file:       # Loops through each row in 'log_file' as a string
        line = line.rstrip()    # Removes whitespace at the end of each row
        day = line[0:3]         # Creates substring from characters at position 0 (included) to position 3 (excluded). Saves substring to variable 'day.'
        if day == "Mon":        # Checks if value of substring 'day' is 'Mon'
            print(line)         # If conditional above is true, prints the row of 'log_file'


# Calls the function 'sales_reports', passing in file object 'log_file'
sales_reports(log_file)



# Extra credit problem
print('\n\nBeginning of extra credit problem\n\n')
log_file.seek(0)                        # Moves cursor to top of log_file

# Define function return_large_orders that takes in the variable 'log_file'
def return_large_orders(log_file):
    for line in log_file:               # Loops through each row in 'log_file' as a string
        line.lstrip()                   # Removes whitespace at the front of each line
        count = line[16:18]             # Creates substring from characters at position 17 (included) to position 19 (excluded). Saves substring to variable 'count.'
        count = count.rstrip()          # Removes whitespace at the end of count
        if int(count) > 10:             # Converts count to an integer and checks if it is over 10
            print(line)                 # If the conditional is true, prints the row from 'log_file'
            
            
# Calls the function 'return_large_orders', passing in file object 'log_file'
return_large_orders(log_file)

