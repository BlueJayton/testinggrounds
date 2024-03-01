
import time
import math

#step 1
def fizz_buzz_game():
    start = time.time()
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: print(i)
        
    end = time.time()
    print (f"Total time: {end - start}")

#step 2
def sphere_volume(radius):
    return (4/3) * math.pi * math.pow(radius, 3)

#step 3
def divide_with_error_handling(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        return "You cannot divide by 0"
    return result

#step 4
def decode_csv_data_into_dictionary(filename):
    
    #open file
    input_csv_file = open(filename)
    
    #get column names
    column_names_string = input_csv_file.readline()
    list_of_column_names = column_names_string.strip().split(",")
    
    #create dictionary
    output_dictionary = dict.fromkeys(list_of_column_names)
    
    #Read the file and create a table (list of lists)
    csv_table_data = []
    for line in input_csv_file:
        csv_table_data.append(line.strip().split(","))

    #iterate over table by cols and append data according to key
    for index, key in enumerate(output_dictionary):
        output_dictionary[key] = []
        for row in csv_table_data:
            output_dictionary[key].append(row[index])
            
    return output_dictionary