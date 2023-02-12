# # # list1 = [3, 5, 6, 2]
# # # list2 = [10, 4, 20, 11, 7]
# # # list1mod = " ".join(str(e) for e in list1)
# # # print(list1mod)


# # #This code reads the contents of the file 'credentials.txt', splits the contents into a list of lines, 
# # # and then iterates over the lines. For each line, it splits the line into a tuple of username and password 
# # # and checks if the username and password match the expected values. If they do, it prints a message indicating 
# # # that the username and password are valid. If they don't, it prints a message indicating that the username 
# # # and password are not valid.

# # strings = ['string1', 'string2', 'string3']
# # titles = ['Title 1', 'Title 2', 'Title 3']

# # # Print each string with its corresponding title  
# # for s, t in zip(strings, titles):
# #     print('{}: {}'.format(t, s))

# # ['admin', 'Register Users with taskManager.py', 'Use taskManager.py to add the usernames and passwords for all team members that will be using this program.', '10 Jan 2023', '22 Dec 2022', 'No']

# # heading = f"{'username':8s}{gap}{'task':15s}{gap}{'description':20s}{gap}{'due_date':8s}{gap}\
# #              {'date_assigned':8s}{gap}{'status':3s}"
# #             print("="*100)
# #             print(heading)
# #             print("-"*100)

# # titles = ['username', 'task', 'description', 'due_date', 'date_assigned', 'status']
# #             data = [
# #                 ['username', 'task', 'description', 'due_date', 'date_assigned', 'status'], temp]


# # # Print each string with its corresponding title  
# #             for s, t in zip(temp, titles):
# #                 gap = ' '*3
# #                 print('{}:{}{}'.format(t,gap,s))

# # headers = ['username', 'task', 'description', 'due_date', 'date_assigned', 'status']           
# #             print(f'{headers[0]: <10}{headers[1]: <15}{headers[2]: <30}{headers[3]: <10}{headers[4]: <10} {headers[5]}')
# #             for row in temp:
# #                 print(f'{row[0]: <10}{row[1]: <15}{row[2]: <30}{row[3]: <10}{row[4]: <10} {row[5]}')


# # int_key_list = [(1, 'apple'), (2, 'banana'), ("c", 8)]
# # int_key_dict = dict(int_key_list)
# # print(int_key_dict)

# # my_tuple = (1, 'apple')
# # a, b = my_tuple
# # print(a) # prints 1
# # print(b) # prints apple

# profile_dict = {'name': 'Chris',
#                 'surname': 'Smith',
#                 'age': 28,
#                 'cell': '083 233 3242'
#                }
# # print(profile_dict.get('name'))
# # profile_dict['surname'] = "Tchukwagi"
# # keys = profile_dict.keys()
# # values = profile_dict.values()
# # print(keys)
# # print(values)
# # # print(type(keys))

# # total_worth = 0


# # string = "your_string"
# # # Create an empty dictionary
# # char_count = {}

# # # Iterate through each character in the string
# # for char in string:
# #   # If the character is not in the dictionary, add it and set the count to 1
# #   if char not in char_count:
# #     char_count[char] = 1
# #   # If the character is already in the dictionary, increment the count by 1
# #   else:
# #     char_count[char] += 1

# # # Print the dictionary
# # print(char_count)

# #Finding max index for multiple occurrences of elements
# # If there are multiple occurrences of the maximum element for a list, then we will have to apply a different logic for the same. We will make use of list comprehension to store multiple indexes inside a list.

# # my_list = [10,72,90,90,54,25,90,40]
# # max_item = max(my_list)
# # index_list = [index for index in range(len(my_list)) if my_list[index] == max_item]
# # print(index_list)

# #To generate random jokes, use:

# # import requests
# # response = requests.get("https://api.chucknorris.io/jokes/random")
# # joke = response.json()['value']
# # print(joke)

# # def add_one(x):
# #     y = x + 1
# #     # print(y)
# #     return y
# # num_plus_one = add_one(10)
# # print(num_plus_one)

# # # The result that the 'add_one' function returns is stored in the num_plus_one variable.
# # print ("10 plus 1 is equal to: " , (num_plus_one), ".")

# numbers_string = "min:1, 2, 3, 4, 5, 6"

# # Split the string into a list of numbers

# numbers = numbers_string.replace("min:", "")
# print(numbers)
# print(type(numbers))

# numbers_2 = numbers.split(", ")
# print(numbers_2)
# print(type(numbers_2))
# # numbers_2 = numbers.strip(", ")
# numbers_2 = [int(x) for x in numbers_2]
# print(numbers_2)
# # # Convert the strings in the list to integers
# # numbers = [int(x) for x in numbers]
# # print(numbers)
# # print(type(numbers))
# # print(numbers)
# # # Find the minimum value
# minimum = min(numbers_2)

# print(minimum)


# # # Open the input file in read only mode and create the output file
# # with open('T24/input.txt', 'r') as input_file, open("T24/output.txt", "a") as output_file:
    
# #     # read the first line and save it into a variable, then write it in the output file
# #     second_line = input_file.readline() 
# #     maximum_block = output_file.write(second_line) 
# #     print(type(maximum_block)) #useful to know what the file type is so that you can know how to handle it
    
# #     # Since the line is of type integer, convert to string and then iterate
# #     maximum_block = str(maximum_block)
# #     # Convert the strings to integers and find the minimum
# #     maximum = [int(x) for x in maximum_block]
# #     maximum = max(maximum_block)
# #     # print(minimum)
# #     output_file.write("The max of [1, 2, 3, 5, 6] is ")
# #     output_file.write(maximum)



# s = "min:1,2,3,4,5,6"

# # Split the string on the colon character
# lst = s.split(':')
# print(lst)
# print(type(lst))
# # Split the second element (the string of comma-separated integers) on the comma character
# numbers = lst[1].split(',')
# print(numbers)
# # Convert the list of strings to a list of integers
# numbers = list(map(int, numbers))
# print(numbers)
# # Find the minimum and average of the numbers
# minimum = min(numbers)
# average = sum(numbers) / len(numbers)

# print(minimum)  # prints 1
# print(average)  # prints 3.5



# # Start here...

#  # Since the line is of type integer, convert to string and then iterate
#     minimum_block = str(minimum_block)
#     # Convert the strings to integers and find the minimum
#     minimum = [int(x) for x in minimum_block]
#     minimum = min(minimum_block)
#     # print(minimum)
#     output_file.write("The min of [1, 2, 3, 5, 6] is ")
#     output_file.write(minimum)
#     output_file.write("\n")

# # Number 2: Maximum in a string

# # Open the input file in read only mode and create the output file
# with open('T24/input.txt', 'r') as input_file, open("T24/output.txt", "a") as output_file:
    
#     # read the first line and save it into a variable, then write it in the output file
#     second_line = input_file.readline() 
#     maximum_block = output_file.write(second_line) 
#     print(type(maximum_block)) #useful to know what the file type is so that you can know how to handle it
    
#     # Since the line is of type integer, convert to string and then iterate
#     maximum_block = str(maximum_block)
#     # Convert the strings to integers and find the minimum
#     maximum = [int(x) for x in maximum_block]
#     maximum = max(maximum_block)
#     # print(minimum)
#     output_file.write("The max of [1, 2, 3, 5, 6] is ")
#     output_file.write(maximum)

#     output_file.write("\n")


# # Number 3: Average in a string

# # Open the input file in read only mode and create the output file
# with open('T24/input.txt', 'r') as input_file, open("T24/output.txt", "a") as output_file:
    
#     # read the first line and save it into a variable, then write it in the output file
#     third_line = input_file.readline() 
#     average_block = output_file.write(third_line) 
#     print(type(average_block)) #useful to know what the file type is so that you can know how to handle it
    
#     # Since the line is of type integer, convert to string and then iterate
#     average_block = str(average_block)
#     # Convert the strings to integers and find the minimum
#     average = [int(x) for x in average_block]
#     average = ''.join(map(str, average))
#     average = int(average)
#     average_2 = sum(average) / len(average)
    
#     output_file.write("The avg of [1, 2, 3, 5, 6] is ")
#     output_file.write(average_2)
#     output_file.write("\n")

new_num = 5
if new_num == 6:
    print("No")
else:
    print("Yes)")