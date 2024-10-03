'''
 Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''

input_string = input("Enter the tuple values separated by spaces: ")
numbers_tuple = tuple(map(int, input_string.split()))
total_sum = 0
for number in numbers_tuple:
    total_sum += number
print(total_sum)
