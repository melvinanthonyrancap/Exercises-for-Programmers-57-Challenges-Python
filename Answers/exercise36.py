import os
import math
os.system('cls')

def get_average(data_list):
	total_sum = 0
	size = len(data_list)

	for i in range(size):
		total_sum += data_list[i]

	return total_sum / size

def get_min(data_list):
	return min(data_list)

def get_max(data_list):
	return max(data_list)

def get_deviation(data_list):
	average = get_average(data_list)
	total_sum = 0
	size = len(data_list)

	for i in range(size):
		total_sum += (data_list[i] - average)**2

	return math.sqrt(total_sum / (size - 1))

def collect_data():
	data_list = []

	user_input = input("Enter a number: ")

	while True:
		if user_input == "done" and len(data_list) > 2:
			return data_list
			break
		elif user_input == "done" and len(data_list) <= 1:
			print("Not enough data")
		else:
			data_list.append(int(user_input))
			user_input = input("Enter a number: ")

	return data_list

#Main Program
user_input = collect_data()
print("\nNumbers: ")
print(*user_input,sep=",")
print(f"The average is {get_average(user_input):.0f}.")
print(f"The minimum is {get_min(user_input)}.")
print(f"The maximum is {get_max(user_input)}.")
print(f"The Standard deviation is {get_deviation(user_input):.2f}.")


"""
Computing Statistics
Statistics is important in our field. When measuring response
times or rendering times, it’s helpful to collect data so you
can easily spot abnormalities. For example, the standard
deviation helps you determine which values are outliers and
which values are within normal ranges.
Write a program that prompts for response times from a
website in milliseconds. It should keep asking for values
until the user enters “done.”
The program should print the average time (mean), the
minimum time, the maximum time, and the standard deviation.
To compute the average (mean)
1. Compute the sum of all values.
2. Divide the sum by the number of values.
To compute the standard deviation
1. Calculate the difference from the mean for each number
and square it.
2. Compute the mean of the squared values.
3. Take the square root of the mean.

Example Output
Enter a number: 100
Enter a number: 200
Enter a number: 1000
Enter a number: 300
Enter a number: done
Numbers: 100, 200, 1000, 300
The average is 400.
The minimum is 100.
The maximum is 1000.
The standard deviation is 400.25(error in book actual value is 408.25).

Constraints
• Use loops and arrays to perform the input and mathematical
operations.
Chapter 7. Data Structures • 68
report erratum • discuss
• Be sure to exclude the “done” entry from the array of
inputs.
• Be sure to properly convert numeric values to strings.
• Keep the input separate from the processing and the
output.
"""